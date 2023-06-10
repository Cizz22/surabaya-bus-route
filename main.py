
from utils import get_scrap_data, get_scrap_data_angkot
import pandas as pd


def main():
    # URL = "https://moovitapp.com/index/in/Tranportasi_Umum-lines-Surabaya-4524-962472"

    #access URL from csv
    URLS = pd.read_csv("link.csv")
    
    for index, row in URLS.iterrows():
        URL = row['links']
    
        # name = get_scrap_data(URL)
        get_scrap_data(URL)

    # print(f"File {name} berhasil disimpan")


if __name__ == "__main__":
    main()