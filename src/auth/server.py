import jwt, datetime, os

from flask import request, Flask
from flas_mysqldb import MySQL

from dotenv import load_dotenv, find_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

SQL_HOST = os.getenv('SQL_HOST')
SQL_USER = os.getenv('SQL_USER')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')
SQL_DB = os.getenv('SQL_DB')
SQL_PORT = os.getenv('SQL_PORT')

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_EXPIRATION_HOURS = os.getenv('JWT_EXPIRATION_HOURS')

server = Flask(__name__)
mysql = MySQL(server)

@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "Missing credentials", 401
    
    cur = mysql.connection.cursor()
    res = cur.execute("SELECT email, password FROM users WHERE email=%s", (auth.email,))

    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        if auth.email != email or auth.password != password:
            return "Invalid credentials", 401
        else:
            return createJWT(auth.username, JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRATION_HOURS)
    else:
        return "Invalid credentials", 401
