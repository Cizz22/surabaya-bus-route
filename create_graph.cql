// Create Route Node
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Cizz22/surabaya-bus-route/main/Data/Route_fix.csv' AS row
CREATE (:Route {route_name: row.route_name, frequency: row.frekuensi, operation_time: row.jam_operasi});


// Create Stop Node
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/Cizz22/surabaya-bus-route/main/Data/Stops/R1%20Rajawali.csv' AS row
WITH row.stop_name AS sequence
WITH collect(sequence) AS sequences
UNWIND sequences AS stopName
MERGE (stop:Stop {stop_name: stopName})
RETURN stop


// Create GO_TO Relationship
LOAD CSV WITH HEADERS FROM 'file:///data.csv' AS row
WITH row.stop_name AS sequence
WITH collect(sequence) AS sequences
CALL apoc.cypher.doIt(
'UNWIND range(0, size($sequences)-2) AS i
MATCH (source:Stop {stop_name: $sequences[i]})
MATCH (target:Stop {stop_name: $sequences[i+1]})
MERGE (source)-[:GO_TO]->(target)',
{sequences: sequences}
) YIELD value
RETURN value


// Create Has_Stop Relationship 
LOAD CSV WITH HEADERS FROM 'file:///data.csv' AS row
MATCH (route:Route {route_name: "RouteName"})  // Assuming "Route" label and "route_id" property
MATCH (stop:Stop {stop_name: row.stop_name})  // Assuming "Stop" label and "stop_id" property
MERGE (route)-[:HAS_STOP]->(stop)
