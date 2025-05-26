from mysql.connector import connect, Error
try:
    connection = connect(
        host="pythonactivities.cotpafanc2of.eu-west-2.rds.amazonaws.com",
        user="admin",
        password="admin1234",
        database="PythonActivities",
    )
except Error as e:
    print(e)
# initailising all variables
commandExec = {}
possibleCommands = ["help", "add new recipe", "quit", "list all recipes", "search recipe", "sort recipes"]
commandExec = {}
# print possible commands
def HelpCommand():
  print("Possible Commands: ", possibleCommands)
  print("")
# add the new function to the commandExec dictionary
commandExec["help"] = HelpCommand

# search for a specific recipe
def SearchCommand():

  # taking input for search
  searchKey = input("Type here to search for recipes: ")

  # running sql query to retrive item list where item name is like entered string
  sql = """SELECT * FROM PizzaRecipes WHERE pizzaName LIKE %s"""
  adr = ("%"+searchKey+"%", )
  cursor.execute(sql, adr)
  records = cursor.fetchall()

  # printing search results
  print("Search result:")
  for row in records:
      print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
  print("")

commandExec["search recipe"] = SearchCommand
# sort the list of recipes
def SortCommand():

  # printing possible sorting options
  print("Please choose sorting type: \n1 - ID Ascending\n2 - ID Descending\n3 - Name Ascending\n4 - Name Descending")
  
  # taking sort type as input
  sortID = input("Please enter sort type (number): ").strip().lower()
  
  # checking if sort type 1 is chosen
  if sortID == "1":
  
      # running sql query to retrive sorted item list
      sql_select_Query = "select * from PizzaRecipes ORDER BY pizzaID"
      cursor.execute(sql_select_Query)
  
  # checking if sort type 2 is chosen
  if sortID == "2":
  
      # running sql query to retrive sorted item list
      sql_select_Query = "select * from PizzaRecipes ORDER BY pizzaID DESC"
      cursor.execute(sql_select_Query)
  
  # checking if sort type 3 is chosen
  if sortID == "3":
  
      # running sql query to retrive sorted item list
      sql_select_Query = "select * from PizzaRecipes ORDER BY pizzaName"
      cursor.execute(sql_select_Query)
  
  # checking if sort type 4 is chosen
  if sortID == "4":
  
      # running sql query to retrive sorted item list
      sql_select_Query = "select * from PizzaRecipes ORDER BY pizzaName DESC"
      cursor.execute(sql_select_Query)
  
  # fetching queried data
  records = cursor.fetchall()
  
  # printing item list with for loop
  for row in records:
      print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
  print("")

commandExec["sort recipes"] = SortCommand
# quit the program
def QuitCommand():

  # ACTIVITY 2
  # display goodbye message before closing
  print("Goodbye")

  # this weird code beneath is for exiting the runtime in google colab, for a normal python programme we would use exit() or quit() instead
  exit()

commandExec["quit"] = QuitCommand
# running sql query to retrive item list
def ListCommand():

    # ACTIVITY 2
    # Please insert list item (select) sql command here
    sql_select_Query = ""

    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    # printing item list with for loop
    print("List of Recipes:")
    for row in records:
        print(str(row[0]) + " - " + str(row[1]) + ": " + str(row[3]) + " = " + str(row[2]))
    print("")

commandExec["list all recipes"] = ListCommand()