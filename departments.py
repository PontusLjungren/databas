import DBApp
import queries

mydb = DBApp.get_connection()
mycursor = mydb.cursor()
mycursor.execute("USE ht21_1_project_group_14")
mycursor.execute("SELECT department_number FROM DEPARTMENT")
database_departments = []
for x in mycursor:
  database_departments.append(x[0])
while True:
  department_id = input("What department do you wish to see? ")
  if int(department_id) in database_departments:
    products = queries.is_leaf_department(mycursor, department_id)
    for product in products:
      output = ""
      for attribute in product:
        output = output + str(attribute) + " "
      print(output)