# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Activity 01 - CSV Data Load

import mysql.connector 
import csv
import os
import sys

# definitions/parameters
DATA_FOLDER = os.path.join("..", "data")
CSV_FILE_NAME = 'employees.csv'
DB_HOST = 'localhost'
DB_NAME = 'hr'

if __name__ == "__main__":
    DATA_FOLDER = os.path.join("..", "data")
    print(DATA_FOLDER)
    print(os.path.exists(DATA_FOLDER))
    quit()

    # TODO: get db connection parameters
    db_user   = os.getenv('db_user')
    db_passwd = os.getenv('db_pass')

    try:
        # TODO: connect to db
        db = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=db_user,
            password=db_passwd,
            autocommit=True
        )
        # print('DB connection successful!')

        # TODO: check if csv file exists
        filepath = os.path.join(DATA_FOLDER, CSV_FILE_NAME)

        if not os.path.exists(filepath):
            print("File not found:  " + filepath)
            exit()

        # TODO: process csv file
        cursor = db.cursor()
        count = 0
        sql = "INSERT INTO Employees " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                try:
                    cursor.execute(sql, row)
                    count += 1
                except Exception as e:
                    pass

        print(f"{count} rows inserted.")

    except Exception as error:
        print(error)
