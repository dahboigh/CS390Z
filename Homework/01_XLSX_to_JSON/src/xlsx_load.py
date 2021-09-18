# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Student: Nicole Weickert
# Description: Homework 01 - XLSX Data Load

from zipfile import ZipFile
from bs4 import BeautifulSoup
import os
import json

# definitions/parameters
DATA_FOLDER =           os.path.join("..", "data")
ATHLETES_FILE_NAME =    os.path.join(DATA_FOLDER, "xl", "worksheets", "sheet1.xml")
SS_FILE_NAME =          os.path.join(DATA_FOLDER, "xl", "sharedStrings.xml")
JSON_FILE_NAME =        os.path.join(DATA_FOLDER, "athletes.json")
XLSX_FILE_NAME =        os.path.join(DATA_FOLDER, "Athletes.xlsx")


def file_exists(filepath, exit_if_missing=False):
    # Returns True if file exists
    # Otherwise returns False (default) or exits with error message

    if os.path.exists(filepath):
        return True
    else:
        if exit_if_missing:
            print("File not found:  " + filepath)
            exit()
        else:
            return False


def strip_digits(string):
    # thanks, https://stackoverflow.com/questions/12851791/removing-numbers-from-string
    return ''.join(i for i in string if not i.isdigit())


if __name__ == "__main__":

    # TODO: If either xml file is missing, extract data from XLSX
    if not (file_exists(SS_FILE_NAME) and file_exists(ATHLETES_FILE_NAME)):

        # Quit with error if Athletes.xlsx is also missing
        file_exists(file := XLSX_FILE_NAME, True)
        with ZipFile(file, 'r') as zipObj:
            zipObj.extractall(DATA_FOLDER)

        # Confirm both xml files now exist; exit with error if still missing
        file_exists(SS_FILE_NAME, True)
        file_exists(ATHLETES_FILE_NAME, True)

    # TODO: creates a list with all strings found in "sharedStrings.xml"
    with open(SS_FILE_NAME) as file:
        soup = BeautifulSoup(file, "xml")
        file.close()
    shared_strings = list(soup.stripped_strings)

    # TODO: read contents of "athletes.xml" into a list of dictionaries
    with open(ATHLETES_FILE_NAME) as file:
        soup = BeautifulSoup(file, "xml")
        file.close()

    athlete_list = []
    column_header = {}
    rows = soup.find_all('row')

    for row in rows:
        athlete = {}
        for cell in row.children:
            column_letter = strip_digits(cell['r'])
            cell_value = shared_strings[int(cell.string)]

            if row['r'] == "1":
                column_header[column_letter] = cell_value.lower()

            else:
                key = column_header[column_letter]
                athlete[key] = cell_value

        if not athlete == {}:
            athlete_list.append(athlete)

    # TODO: write list into json file
    with open(JSON_FILE_NAME, "w") as outfile:
        json.dump(athlete_list, outfile, indent=1)
        outfile.close()
