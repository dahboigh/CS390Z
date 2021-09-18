# Program Requirements:
#   Create a folder named 'data' and open permission to all users
#   Grant file permissions to a db user
#   Export table data to a new csv file in the data folder

# Developed on Windows 10 Pro, Version 2004, Build 19041.1165
# Structure is provided for cross-platform compatibility but has not yet been tested

import platform
import os
import mysql.connector


folder = "data"
file = "employees.csv"

db_table = 'employees'
db_host = "localhost"
db_name = "hr"
db_restricted_user = 'hr_admin'
db_user = os.getenv("db_user")
db_pass = os.getenv("db_pass")


def quit_msg(msg, error):
    print(msg)
    print("Error:", error)
    quit()


if __name__ == "__main__":

    system = platform.system()
    filepath = os.path.join(os.path.join(os.getcwd(), folder, file))

    # Adjust commands for operating system
    CREATE_FOLDER = f"mkdir {folder}"

    if system == "Windows":
        FULL_ACCESS = f"CACLS {folder} /E /G Everyone:F"
        DELETE_FILE = f"del /f {filepath}"

    else:
        FULL_ACCESS = f"chmod 777 {folder}"
        DELETE_FILE = f"rm {filepath}"

    if system not in ["Windows", "Linux", "Darwin"]:
        print(f"Warning: This program isn't compatible with {system}. "
              f"File output may not be saved correctly.")


    # Establish db connection; quit on failure
    try:
        db = mysql.connector.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass
        )

        sql = f"GRANT FILE ON *.* TO {db_restricted_user}"
        cursor = db.cursor()
        cursor.execute(sql)


    except Exception as error:
        quit_msg("Couldn't connect to database", error)


    # Create Destination folder with open permissions
    if not os.path.exists(folder):
        os.system(CREATE_FOLDER)
        os.system(FULL_ACCESS)


    # Verify that folder was created, quit otherwise
    if not os.path.exists(folder):
        quit_msg("Could not create folder with full access.", None)


    # If a csv file already exists, delete it
    if os.path.exists(filepath):
        os.system(DELETE_FILE)

    # Retrieve SQL data and save to file
    outfile = filepath.replace("\\", "/")
    sql = f" \
        SELECT * FROM {db_table} \
        INTO OUTFILE '{outfile}' \
        FIELDS TERMINATED BY ',' \
        LINES TERMINATED BY '\\n';"

    cursor.execute(sql)

    cursor.execute(f"SELECT COUNT(*) FROM {db_table}")
    result = cursor.fetchall()
    rowcount = result[0][0]

    db.close()

    # Verify that folder was created
    if not os.path.exists(filepath):
        quit_msg(f"File was not created.")
    else:
        print(f"Exported {rowcount} records to {file}.")
