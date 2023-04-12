from flask import Flask, jsonify, request
import requests
import flask_mysqldb
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["DEBUG"] = True

app.config['MYSQL_HOST'] = 'mysql_api_container'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdocker'

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    random_user_api_response = requests.get('https://randomuser.me/api')
    random_user_data = random_user_api_response.json()
    return jsonify(random_user_data)

@app.route("/inserthost", methods=["POST"])
def inserthost():
    random_user_data = requests.get('https://randomuser.me/api').json()
    username = random_user_data['results'][0]['name']['first']

    db_cursor = mysql.connection.cursor()
    db_cursor.execute("""INSERT INTO USERS(NAME) VALUES(%s)""", (username,))
    mysql.connection.commit()
    db_cursor.close()

    return username 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
