import mysql.connector

import queries

mydb = None

def get_cursor():
  group_number="14" #FILL IN YOUR GROUP NUMBER
  mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="ht21_1_group_"+group_number,
    passwd="pwd_"+group_number,
    database="ht21_1_hotels_group_"+group_number
  )

  return mydb.cursor()

def close_connection():
  mydb.close()
