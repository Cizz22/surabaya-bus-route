
from utils import get_scrap_data


def main():
    URL = "https://moovitapp.com/index/in/Tranportasi_Umum-line-R7_R8-Surabaya-4524-1548672-58190412-1"

    name = get_scrap_data(URL)

    print(f"File {name} berhasil disimpan")


if __name__ == "__main__":
    main()