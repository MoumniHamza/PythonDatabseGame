import sqlite3
connection = sqlite3.connect('game.db')

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


 

