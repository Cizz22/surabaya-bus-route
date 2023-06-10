from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

import time
import csv
import pandas


def get_scrap_data_angkot(URL):
    options = Options()
   
    ##options.add_argument("--headless")

    driver = webdriver.Edge(options=options)
    
    with driver as browser:
        browser.get(URL)
        angkot_route = browser.find_elements(By.XPATH, "//li[contains(@class, 'line-data')]")
        
        links = []
       
        for angkot in angkot_route:
            data = angkot.find_element(By.TAG_NAME, "a")
            name = data.find_element(By.TAG_NAME, "span").text + " " +data.find_element(By.TAG_NAME, "strong").text 
            links.append([name])
        
            with open("route_name.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(links)
            


def get_scrap_data(url):
    options = Options()
    # options.add_argument("--headless")

    driver = webdriver.Edge(options=options)
    with driver as browser:
        # Menggunakan Selenium untuk membuka website
        browser.get(url)

        name = browser.find_element(By.TAG_NAME, "h1").text + ".csv"

        # Mengambil data dari website
        stops_list = browser.find_element(By.CLASS_NAME, "stops-list")

        stop_containers = stops_list.find_elements(By.CLASS_NAME, "stop-container")

        data = []
        data.append(["stop_name"])
        for stop in stop_containers:
            h3_element = stop.find_element(By.TAG_NAME, "h3")
            text = h3_element.text
            data.append([text])
        # Simpan data ke dalam file CSV

        with open(name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)

        return name
