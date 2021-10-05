import mysql.connector

group_number="14" #FILL IN YOUR GROUP NUMBER

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht21_1_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht21_1_hotels_group_"+group_number
)

mycursor = mydb.cursor()
name="\"Golden Nugget\""
mycursor.execute("SELECT EANHotelID, Name FROM Property WHERE Name = "+name)

myresult = mycursor.fetchall()
print("EANHotelID\t Name")
for x in myresult:
  print(str(x[0])+"\t"+x[1])

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mycursor.execute("USE ht21_1_project_group_14")
myresult = mycursor.fetchall()

mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

mydb.close()