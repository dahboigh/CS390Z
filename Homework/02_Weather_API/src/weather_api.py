# CS390Z - Introduction to Data Minining - Fall 2021
# Instructor: Thyago Mota
# Description: Homework 02 - Weather API

import csv
import urllib.parse
import requests
import json
import os
import gzip
from datetime import datetime

# definitions/parameters
DATA_FOLDER = os.path.join('..', 'data')
LOCATIONS_FILE_NAME = 'locations.csv'
JSON_FILE_NAME = 'weather.json'
OPEN_WEATHER_API = 'http://api.openweathermap.org/data/2.5/weather'
CITY_LIST_URL = 'http://bulk.openweathermap.org/sample/city.list.json.gz'


def quit_msg(msg):
    print(msg)
    quit()


if __name__ == "__main__":
    today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    api_key = os.getenv('API_KEY')


    ## TODO: Get list of locations

    # Quit if CSV file not found
    if not os.path.exists(filepath := os.path.join(DATA_FOLDER, LOCATIONS_FILE_NAME)):
        quit_msg("File not found:  " + filepath)

    locations = []
    with open(filepath) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            locations.append(row)
        file.close()


    # ## TODO: Download and extract list of city IDs
    filename = CITY_LIST_URL.split("/")[-1]
    extension = "." + filename.split(".")[-1]
    filepath = os.path.join(DATA_FOLDER, filename.replace(extension, ""))

    if not os.path.exists(filepath):
        if extension != ".gz":
            quit_msg("Archived file is not in .gz format")

        # download zipped file
        response = requests.get(CITY_LIST_URL, stream=True)
        if response.status_code != 200:
            quit_msg(f"Failed to retrieve content. Status code:{response.status_code}")

        # extract file      (with help from https://stackoverflow.com/a/61195974)
        try:
            with urllib.request.urlopen(CITY_LIST_URL) as response:
                with gzip.GzipFile(fileobj=response) as uncompressed:
                    file_content = uncompressed.read()

            # write to file in binary mode 'wb'
            with open(filepath, 'wb') as file:
                file.write(file_content)

        except Exception as e:
            quit_msg(f"Download and extraction failed: {e}")


    ## TODO:  Retrieve unique city IDs and query API

    file = open(filepath, encoding="utf8")
    data = json.loads(file.read())
    file.close()
    os.remove(filepath)

    list = []
    msg = ""

    for i in locations:
        city, state = i[0], i[1]
        try:
            # (with help from https://stackoverflow.com/a/45414177 to replace my inefficient loop)
            id = [obj for obj in data if ((obj['name'], obj['state'], obj['country']) == (city, state, "US"))][0]['id']
            url = f"{OPEN_WEATHER_API}?id={id}&appid={api_key}&units=imperial"
            response = requests.get(url, headers={'Cache-control': 'no-cache'}).json()

            entry = {
                'today': today,
                'city': city,
                'state': state,
                'temp_min': round(response['main']['temp_min']),
                'temp_max': round(response['main']['temp_max']),
                'temp': round(response['main']['temp']),
            }
            list.append(entry)

        except Exception as e:
            msg += f"{city} {state} not included. ({e})\n"

    print(f"{len(list)} entries written.")
    print(msg)

    ## TODO: Write json results to file

    with open(os.path.join(DATA_FOLDER, JSON_FILE_NAME), 'w') as outfile:
        json.dump(list, outfile, indent=1)
        outfile.close()