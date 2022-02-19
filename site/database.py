import sqlite3

try:
    con = sqlite3.connect('tables.db')
    #con = sqlite3.connect('admin.db')
    print("Connection is established: Database is opened")
except:
    print("Error: database not found")
    exit()

#username password (геолокация/адрес местонахождения или брать адрес больницы) текущая заявка, cht_id, auth

cursorObj = con.cursor()
#cursorObj.execute("CREATE TABLE Anketa(cht_id integer, name text, lastname text, addres text, ballstatus integer, ankstatus integer)")
#cursorObj.execute("CREATE TABLE User(user_id integer, username text, password text, lib text, render text, level text, settings text)")
#cursorObj.execute("CREATE TABLE Library(name text, id text)")
#cursorObj.execute("INSERT INTO Anketa(cht_id,name, lastname, addres, ballstatus,ankstatus) VALUES(?, ?, ?, ?, ?,?)", (89338,"Арнольд","Дюжев","ул.Камазова, дом 9",234,0))
#cursorObj.execute("INSERT INTO Admin(name, lastname, patronymic, username, password, location, ankcurrent, cht_id, auth) VALUES(?, ?, ?, ?, ?,?,?,?,?)", ("Арнольд","Арнольдов","Арнольдович",
#                    "admin","a62b8446f99b4c8acf9f053f89eed254","Саров, Нижегородская область", 893381792,893381792,0))
#cursorObj.execute("UPDATE User SET user_id = 0, username = \"asd\", password = \"123\", lib = \"{1232s,sd}\"")
#cursorObj.execute("INSERT INTO User(user_id, username, password, lib, render, level, settings) VALUES(?, ?, ?, ?, ?,?, ?)", (89338,"loh","qwerty112233","lib2","123","321", "sett"))
print(cursorObj.execute("SELECT * FROM Library").fetchall())

#cursorObj.execute("ALTER TABLE Library ADD loader text")


#cursorObj.execute("INSERT INTO Library(name, id, autor, loader) VALUES(?, ?, ?, ?)", ("War and Piece", "123", "Leo Tolstoy", "loh"))


#cursorObj.execute("DELETE FROM Anketa WHERE name='рустам'")
#cursorObj.execute("UPDATE Admin SET cht_id={} WHERE cht_id = {}".format(0,893381792))
con.commit()
