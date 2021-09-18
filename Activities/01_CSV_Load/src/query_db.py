import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  database="hr",
  user=os.getenv("db_user"),
  password=os.getenv("db_user")
)

cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM employees")

result = cursor.fetchall()
for x in result:
  print(str(x[0]) + " rows")

db.close()
