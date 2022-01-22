from imghdr import what
import sqlite3
from sqlite3 import Error
from datetime import datetime
import os

from sqlalchemy import false

# D:\Ore facultate\Anul 2 SEM I\Materii\Programarea Aplicatiilor WEB\!! Proiect Semestru !!\Proiect_Netejoru_Mihai_Sorin_Grupa 611\database/users.db
# conectare la baza de date
def connectionToDB(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


# adaugare user
def addUser(conn, users, email):

    if(getEmail(conn, email) == 0):

        query =  """INSERT INTO users(First_Name, Last_Name, email, password)
        VALUES(?,?,?,?)"""
        cur = conn.cursor()
        cur.execute(query, users)
        conn.commit()
        conn.close()

        return cur.lastrowid
    else: false

# functie pentru preluare de date din baza de date !!!!! de modificat pentru SIGN IN
def getUsers(conn):
    cur = conn.cursor()
    query = """SELECT * FROM users"""
    result = cur.execute(query)

    return list(result)


def getEmail(conn, email):
    print(email)
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE email=?"
    result = cur.execute(query, (email,))

    listOfResult = list(result)
    counter = 0

    for i in listOfResult:
        counter+=1



    print(listOfResult)
    print(counter)

    return counter




# stergere utilizator (permannent) !!!! de modificat
#def delete_user():
    conn = connectionToDB()
    cur = conn.cursor()

    nameOfUser = input("Type the name of username: ")
    passOfUser = input("Type your password: ")

    cur.execute("SELECT * FROM users WHERE username=?", (nameOfUser, ))
    result = cur.fetchone()

    if result[5] == passOfUser:
        cur.execute("DELETE FROM users WHERE username=?", (nameOfUser,))
        conn.commit()

    print(result[5], "si", passOfUser)
    
    
    print("You deleted users with username: ", nameOfUser)
    

# actualizare date utilizator !!!! de modificat
#def dataUpdate():
    conn = connectionToDB()
    cur = conn.cursor()

    email = input("Your email: ")
    newPassword = input("New password: ")
    cur.execute("UPDATE users SET Password = ? WHERE email = ?", (newPassword, email))
    conn.commit()
    conn.close()

    print("The password was Updated!!!!")


