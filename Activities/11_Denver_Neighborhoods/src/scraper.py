# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Activity 11: a simple scraper

from helper_methods import *

import csv
import os
import re
import requests
from bs4 import BeautifulSoup

# definitions/parameters
DATA_FOLDER = os.path.join("..", "data")
CSV_FILE_NAME = 'denver_neighborhoods.csv'
BASE_URL = 'https://www.5280.com/neighborhoods/'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}


def main():
    # Ensure destination folder exists
    folder_exists(DATA_FOLDER)

    # Retrieve data
    response = requests.session().get(BASE_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.table.find_all('tr')

    # Write to CSV
    with open(os.path.join(DATA_FOLDER, CSV_FILE_NAME), 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            data = []
            for td in row.find_all(['th', 'td']):
                data.append(re.sub("[,$]", '', td.string))     # remove currency symbols
            writer.writerow(data)
        file.close()


if __name__ == "__main__":
    main()
