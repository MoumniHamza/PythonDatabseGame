import sqlite3
connection = sqlite3.connect('game.db')

def printData(data):
    for name in data:
        print " id: ", name[0]
        print "name: ", name[1]
        print "gender: ", name[2]
        print "occupation: ", name[3]
        print "age: ", name[4]


def createTable():
    connection.execute("CREATE TABLE if not exists persons(id INTEGER PRIMARY KEY AUTOINCREMENT, \
                                         name TEXT, \
                                         gender TEXT, \
                                         occupation TEXT, \
                                         age INT);")
createTable()

def newPerson():
    print(" We need the following information from you")
    name = raw_input("Name:   ")
    gender = raw_input("Gender:   ")
    occupation = raw_input("Occupation:   ")
    age = raw_input("Age:  ")
    string_value = (" '{}', '{}', '{}', {} ").format(name,gender,occupation,age) 
    print(string_value)
    insert_value = "INSERT INTO PERSONS(name,gender,occupation,age) VALUES({});".format(string_value)
    print(insert_value)
    connection.execute(insert_value)
    connection.commit()
    print(" The number of changes: " , connection.total_changes)
newPerson()

def checkPerson():
    select_value = "SELECT * FROM persons";
    selection = connection.execute(select_value)
    rows = selection.fetchall()
    print(rows)
checkPerson()

def specificPerson():
    name = raw_input("name: ")
    select_specificperson = "SELECT * FROM persons WHERE NAME = '{}';".format(name)
    print(select_specificperson)
    selections = connection.execute(select_specificperson)
    print_rows = selections.fetchall()
    if len(print_rows) == 0:
        print (" Sorry there is no record found for your request ")
    else:
        printData(print_rows)
specificPerson()


def deletePerson():
    name = raw_input("name: ")
    select_specificperson = "SELECT * FROM persons WHERE NAME = '{}';".format(name)
    selections = connection.execute(select_specificperson)
    print_rows = selections.fetchall()
    if len(print_rows) == 0:
        print (" Sorry there is no record found for your request ")
    elif len(print_rows) == 1:
        print (" We found one record")
        name = print_rows[0]
        change_id = name[0]
        printData(print_rows)
    else:
        print (" More than one record found")
        printData(print_rows)
        change_id = raw_input(" type the id of the character to update: ")
        print(" Change id: ", change_id)
    delete = raw_input(" Are you sure you want to delete this character y/n? ")
    if delete == "y":
       select_specificperson = "DELETE FROM persons WHERE NAME = '{}';".format(change_id)
       connection.execute(select_specificperson)
       connection.commit()
       print( "Number of changes : ",connection.total_changes)
deletePerson()

def choices():
    print (" What would you like to do ?")
    print (" 1. Add a new character")
    print (" 2. View all charaters")
    print (" 3. Search for a character")
    print( " 4. Delete a character")
    print (" 5. EXIT")
    ask = raw_input(" Enter the number of your choice: ")
    if ask == '1':
       newPerson()
    elif ask == '2':
       checkPerson()
    elif ask == '3':
        specificPerson()
    elif ask == '4':
        deletePerson()
    else:
        print("exiting the program")
        return
choices()

def main():
    do_again = True
    while do_again == True :
          choices()
          ask_again = raw_input("Would you like to do something else y/n:  ")
          if ask_again != 'y':
             do_again == False




