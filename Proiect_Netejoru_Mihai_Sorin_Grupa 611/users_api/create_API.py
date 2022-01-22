# from crypt import methods
from logging import exception
from flask import Flask, request
from phyton_sql_connect import connectionToDB, addUser, getUsers, getEmail
# from crypt import methods
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

DB_file = "D:\Ore facultate\Anul 2 SEM I\Materii\Programarea Aplicatiilor WEB\!! Proiect Semestru !!\Proiect_Netejoru_Mihai_Sorin_Grupa 611\database/users.db"

@app.route("/sign-up", methods=["POST"])
def signUp():

    if request.method == "POST":

        user_data = request.json
        email = user_data.get("email")
        list_user_data = []

        for key, value in user_data.items():
            list_user_data.append(value)
        
        try:
            conn = connectionToDB(DB_file)
            value = addUser(conn, list_user_data, email)
            conn.close()
            
            if(value):
                return "", 200
            else: return Exception

            
        except ValueError as ve:
            error = {
                "error": f"--Invalid value provided user. Error message: {ve}."
            }
            return error, 400
        except Exception as e:
            error = {
                "error": f"--Failed to create user. Error message: {e}."
            }
            return error, 500


@app.route("/sign-in", methods=["GET"])
def signIn():
    if request.method == "GET":
        try:
            conn = connectionToDB(DB_file)
            data = getUsers(conn)
            conn.close()
        except Exception as e:
            response = {
                "error": f"--Failed to connect to db or to get users. Error message: {e}."
            }
            return response, 500

        try:
            response = {
                "users": []
            }
            for row in data:
                # row = (id, First_name, Last_name, email, password, Created, Last_updated)
                element = {
                    "First_name": row[1],
                    "Last_name": row[2],
                    "email": row[3],
                }
                response["users"].append(element)
            return response, 200
        except Exception as e:
            response = {
                "error": f"--Failed to process users information. Error message: {e}."
            }
            return response, 500   






app.run(debug=True)