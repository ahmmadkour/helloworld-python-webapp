from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'helloworld'
app.config['MYSQL_HOST'] = 'mysql.service.consul'

mysql = MySQL(app)


@app.route("/")
def main():
    cur = mysql.connection.cursor()
    query="SELECT value FROM webapp where msg = %s"
    param="index"
    cur.execute(query, [param])
    row = cur.fetchone()
    return row

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

