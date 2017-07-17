from flask import Flask
from flask_mysqldb import MySQL
import dns.resolver
import time

app = Flask(__name__)

MYSQL_HOST = 'mysql.service.consul'

# Get MySQL port
isreachable = False
while isreachable is False:
    try:
        answers = dns.resolver.query(MYSQL_HOST, 'SRV')
        MYSQL_PORT = answers[0].port
        isreachable = True
    except:
        time.sleep(2)


# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'helloworld'
app.config['MYSQL_HOST'] = MYSQL_HOST
app.config['MYSQL_PORT'] = MYSQL_PORT

mysql = MySQL(app)


@app.route("/")
def main():

    try:
        cur = mysql.connection.cursor()
        query="SELECT value FROM webapp where msg = %s"
        param="index"
        cur.execute(query, [param])
        res = cur.fetchone()
    except:
       res = "Error: can't fetch data from the database"

    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

