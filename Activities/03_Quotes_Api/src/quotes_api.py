# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Activity 03 - Quotes API


import requests
from helper_methods import *


# definitions/parameters
DATA_FOLDER = os.path.join('..', 'data')
JSON_FILE_NAME = 'quotes.json'
QUOTES_API_URL = 'http://quotes.rest/qod'


if __name__ == "__main__":

    # TODO: send the request to the API and process the response
    result = requests.get(QUOTES_API_URL)
    if result.status_code != 200:
        quit_msg("Failed to retrieve content.", f"Code {result.status_code}")
    raw_json = json.loads(result.content.decode('utf-8'))

    quote = raw_json['contents']['quotes'][0]
    new_quote = {
        'text':     quote['quote'],
        'author':   quote['author'],
        'tags':     quote['tags'],
        'category': quote['category'],
        'date':     quote['date']
    }

    # TODO: append quotes to json file
    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

    quotes_file = os.path.join(DATA_FOLDER, JSON_FILE_NAME)
    if file_exists(quotes_file):
        quotes = json_read_from_file(quotes_file)
    else:
        quotes = []

    quotes.append(new_quote)
    json_write_to_file(quotes, quotes_file)
