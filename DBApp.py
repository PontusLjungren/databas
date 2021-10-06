import mysql.connector

def home():
  print("Home") 

def electronics():
  pass

def snacks():
  pass

def candy():
  pass

def soda():
  pass

def crisps():
  pass

def computers():
  pass

def tablets():
  pass

def tv():
  pass

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

mycursor.execute("SELECT department_number FROM DEPARTMENT")
database_departments = []
for x in mycursor:
  database_departments.append(x[0])

departments = {
    '0': home,
    '1': electronics,
    '2': snacks,
    '3': candy,
    '4': soda,
    '5': crisps,
    '6': computers,
    '7': tablets,
    '8': tv
}

# get all department_number in a list.
# check that input is valid
while True:
  department_id = input("What department do you wish to see?\n")
  if int(department_id) in database_departments:
    break
  
departments[department_id]()



mydb.close()