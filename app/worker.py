from flask import Flask , render_template, request
import redis
import mysql.connector
import os

cache = redis.Redis(host='localhost' , port=6379 , db=0)


app = Flask(__name__)


mydb = mysql.connector.connect(
    host="localhost",
    port='6603',
    user="root",
    password="babak13830",
    database="babaktest"
)
mycursor = mydb.cursor()

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_PORT'] = '6603'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = os.environ['MysqlPass']
#app.config['MYSQL_PASSWORD'] = 'babak13830'
#app.config['MYSQL_DB'] = 'babaktest'
#mysql = MySQL(app)
#cursor = None

@app.before_request
def before():
	 #cursor = mysql.connection.cursor()
	 mycursor = mydb.cursor()


@app.after_request
def after(test_name):
    #cursor.close()
    mycursor.close()
    mydb.close()
    return test_name


@app.route('/<name>')
def get_http(name):
  sql_ins = "INSERT INTO names VALUES (%s, %s)"
  print(name)
  val = cache.get(name)
  number = int(val)
  values = ( 4, name)
  mycursor.execute(sql_ins , (4 , name))
  mydb.commit()
  return name


if __name__ == '__main__':
      app.run(host='0.0.0.0', port='5005' , debug=True, use_reloader=True)
