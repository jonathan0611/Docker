
from flask import Flask
#import mysql.connector
#from mysql.connector import Error 
import requests 
from flask_mysqldb import MySQL

app = Flask(__name__)
#app.config["DEBUG"] = True

app.config["DEBUG"] = True
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'jonathan'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'flaskhost'

mysql = MySQL(app)

#mysql = mysql.connector.connect(
#       host='localhost',
#      user='jonathan',
#     password='123'
#)


        

@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api')
    return data.json()

@app.route("/inserthost", methods= ['POST'])
def inserthost():
    data = requests.get('https://randomuser.me/api').json()
    username = str(data['results'][0]['id']['name'])

    curl = mysql.connection.cursor()
    curl.execute(f"insert into users(nome) values({username}) ")
    mysql.connection.commit()
    curl.close()

    return username


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")
