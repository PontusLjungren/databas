import DBApp
import queries

mydb = DBApp.get_connection()
mycursor = mydb.cursor()
mycursor.execute("USE ht21_1_project_group_14")

while True:
  product_id = input("Select product: ")
  discount = queries.get_discount(mycursor, product_id)
  print ("Discount: " + str(discount) + "%")

  edit = input("Do you want to edit the discount? (y/n) ")

  if edit == "y":
    new_discount = input("Set new discount: ")
    queries.set_discount(mycursor, product_id, new_discount)
  