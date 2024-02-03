# Starting file for Final Project
# import the sqlite3 database module
#Chris Oesterling 12/4/22 ISIT333

import sqlite3
import random

def setup_db(conn, cursor):
  #creat cursor 
  cursor = conn.cursor()
  # check if the user table already exists, if so, drop it so we can start with a new table
  cursor.execute("DROP TABLE IF EXISTS user;")
  
  # create the table if it doesn't already exist
  # note that primary keys are automatically created in sqlit3 and referenced as rowid 
  cursor.execute("CREATE TABLE user (ID TEXT, first_name TEXT, last_name TEXT, email TEXT, phone_number TEXT, address TEXT, city TEXT, state TEXT, zipcode TEXT, hourly_rate TEXT, department TEXT)")

  # create some records of data
  cursor.execute("INSERT INTO user VALUES (\"1937\", \"Isaac\", \"Newton\", \"IsaacNewton@corporate.com\", \"2034351351\", \"1331 Canyon Rd.\", \"Santa Barbra\", \"CA\", \"77354\", \"$19.5/hour\", \"I.T.\")")

  #2
  cursor.execute("INSERT INTO user VALUES (\"9347\", \"John\", \"Mayor\", \"JohnMayer@corporate.com\", \"9539013432\", \"154 Mount Camp CT\", \"Wonderland\", \"MI\", \"03837\", \"$65/hour\", \"Sound\")")

  #3
  cursor.execute("INSERT INTO user VALUES (\"1000\", \"Joe\", \"Biden\", \"JoeBiden@corporate.com\", \"0383739234\", \"U.S. White House\", \"Washington D.C.\", \"DC\", \"43421\", \"$100/hour\", \"Government\")")

  #4
  cursor.execute("INSERT INTO user VALUES (\"6434\", \"Walter\", \"White\", \"WalterWhite@corporate.com\", \"2052532538\", \"308 Negra Aura Lane\", \"Albuquerque\", \"NM\", \"43210\", \"$300/hour\", \"Production\")")

  #5
  cursor.execute("INSERT INTO user VALUES (\"3213\", \"Ben\", \"Ten\", \"BenTen@corporate.com\", \"1242306315\", \"123 Savery Rd.\", \"Lost\", \"KT\", \"45652\", \"$15.25/hour\", \"Human Resources\")")

  return cursor

def add_user(conn, cursor):

  #create a cursor to use through database
  cursor = conn.cursor()
  
  #get user info
  print("Add new user\n")
  ID = random.randint(1000,9999)
  FN = input("First name: ")
  LN = input("Last name: ")
  email = (FN + LN + "@corporate.com")
  phone = input("Phone: ")
  street = input("Street: ")
  city = input("City: ")
  state = input("State (2 letters): ")
  zipcode = input("Zip code: ")
  hourly = input("Wage per hour: ")
  hourly = "$" + hourly + "/hour"
  DP = input("Department name: ")

  #prepare insert statement for each input
  sql = """
    INSERT INTO user (ID, first_name, last_name, email, phone_number, address, city, state, zipcode, hourly_rate, department)
    VALUES (?,?,?,?,?,?,?,?,?,?,?)
    """

  #execute query with variable names
  cursor.execute(sql, (ID, FN, LN, email, phone, street, city, state, zipcode, hourly, DP))
  print("User added\n")
  return cursor

def list1(conn, cursor):
  
  cursor.execute("SELECT rowid, ID, first_name, last_name, email, phone_number, address, city, state, zipcode, hourly_rate, department FROM user")

  # store the results of a the query to a list called users
  users = cursor.fetchall()
  
  # now we can loop through the results of the query
  for this_user in users:
    print(this_user[0], this_user[1], this_user[2], this_user[3], this_user[4], this_user[10], this_user[11])
    print()

def list2(conn, cursor):
  
  cursor.execute("SELECT rowid, ID, first_name, last_name, email, phone_number, address, city, state, zipcode, hourly_rate, department FROM user")

  # store the results of a the query to a list called users
  users = cursor.fetchall()
  
  # now we can loop through the results of the query
  for this_user in users:
    print(this_user[0], this_user[2], this_user[3], this_user[6], this_user[7], this_user[8], this_user[9], this_user[5])
    print()


def search(conn, cursor):

  cursor.execute("SELECT rowid, ID, first_name, last_name, email, phone_number, address, city, state, zipcode, hourly_rate, department FROM user")

  # store the results of a the query to a list called users
  users = cursor.fetchall()

  #ask for last name
  LN = input("Input the last name of the employee you're looking for: ")
  print()

  #search last name in database
  for this_user in users:
    if LN == this_user[3]:
        print(this_user[1], this_user[2], this_user[3], this_user[11])

def hour(conn, cursor):
  name = input("Last name of employee you would like to update: ")
  print()

  wage = input("New hourly wage of the employee: ")
  wage = "$" + wage + "/hour"

  cursor.execute("UPDATE user SET hourly_rate = ? WHERE last_name = ?"
  ,(wage, name))

  print(wage, "is", name + "'s new hourly wage")
  print()

  return cursor

def contact(conn, cursor):
  name = input("Last name of employee you would like to update: ")
  print()

  street = input("Address: ")
  city = input("City: ")
  state = input("State (two letters): ")
  zip = input("zipcode: ")
  phone = input("phone number: ")

  cursor.execute("UPDATE user SET address = ?, city = ?, state = ?, zipcode = ?, phone_number = ?  WHERE last_name = ?"
  ,(street, city, state, zip, phone, name))

  print(street, city, state, zip, phone, "has been updated for,", name)
  print()

  return cursor


def delete(conn, cursor):
  #ask for last name
  LN = input("Input the last name of the employee you're looking for: ")
  print()

  print("Are you sure you want to delete the file of '" + LN + "'")
  approval = input("Y/N: ")
  #ask user if they really want to delete
  if approval.lower() == 'y':
    #search last name in database
    cursor.execute("DELETE FROM user WHERE last_name = ?", 
    (LN,))
    print(LN, "was deleted\n")
    
    return cursor
  else:
    print(LN + "'s file was not deleted\n")

def menu():
  #menu for user options
  print(" ------ Employee Database Program Menu ------ \n")
  print("Please choose an option below,")
  print("1: Add user")
  print("2: list all employee id's, names, emails, and departments")
  print("3: for names, addresses and phone numbers")
  print("4: search for employee by last name")
  print("5: update hourly wage")
  print("6: update contact info")
  print("7: delete a user")
  print("8: end program")
  print()
    
def main():

  print("Welcome to the employee database\n")
  # create a connection to the database file
  conn = sqlite3.connect("EmployeeDatabase.db")

  #create a cursor to use through database
  cursor = conn.cursor()

  #setup database
  setup_db(conn, cursor)

  #Start menu for user
  while True:
    menu()
    choice = input("Select option: ")
    print()
    if choice == "1":
      add_user(conn, cursor)
    elif choice == "2":
      list1(conn, cursor)
    elif choice == "3":
      list2(conn, cursor)
    elif choice == "4":
      search(conn, cursor)
    elif choice == "5":
      hour(conn, cursor)
    elif choice == "6":
      contact(conn, cursor)
    elif choice == "7":
      delete(conn, cursor)
    elif choice == "8":
      break
    else:
      print("Error, please select a menu option.\n")

  print("Thanks for using the employee database!")

if __name__ == "__main__":
  main()