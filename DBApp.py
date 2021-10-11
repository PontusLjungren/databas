import mysql.connector

import queries

group_number="14" #FILL IN YOUR GROUP NUMBER
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht21_1_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht21_1_hotels_group_"+group_number
)

mycursor = mydb.cursor()

mycursor.execute("USE ht21_1_project_group_14")
mycursor.execute("SELECT department_number FROM DEPARTMENT")
database_departments = []
for x in mycursor:
  database_departments.append(x[0])

def print_product(title, ID, price):
  print("Title: " + title + "    ID: " + str(ID) + "    Price: " + str(price))

# get all department_number in a list.
# check that input is valid
while True:
  department_id = input("What department do you wish to see?\n")
  if int(department_id) in database_departments:
    products = queries.is_leaf_department(mycursor, department_id)
    for product in products:
        print_product(product[0], product[1], product[2])



mydb.close()
