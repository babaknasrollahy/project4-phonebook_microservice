from flask import Flask , render_template, request , g
import redis
import mysql.connector
import os

cache = redis.Redis(host='localhost' , port=6379 , db=0)


test = 1
print(test)
def create_database():
        mydb = mysql.connector.connect(
                host="localhost",
                port="6603",
                user="root",
                password="babak13830"
        )

        # create a cursor object
        mycursor = mydb.cursor()
        # Open and Read .sql file
        with open('create_database.sql', 'r') as f:
        #mycursor.execute(f.read()
                file = f.read()

        commands = file.split(";")
        for command in commands:
                command = command.replace('\n','')
                mycursor.execute(command)
        #commit the changes and close the connection
        mydb.commit()
        mydb.close()






app = Flask(__name__)




try :
	print("database is already exist !!")
	create_database()

except:
	print("error")

def Get_DB():
	mydb = mysql.connector.connect(
		host="localhost",
		port='6603',
		user="root",
		password="babak13830",
		database="phonebook"
	)
	return mydb

#mycursor = mydb.cursor()

@app.before_request
def before():
	g.db = Get_DB()
	g.mycursor = g.db.cursor()


@app.after_request
def after(test_name):
    #cursor.close()
	g.mycursor.close()
	g.db.close()
	return test_name


@app.route('/<name>')
def get_http(name):
  sql_ins = "INSERT INTO names (contactName , contactNumber) VALUES (%s, %s)"
  val = cache.get(name)
  number = int(val)
  g.mycursor.execute(sql_ins , (name , number))
  g.db.commit()
  return name

@app.route('/api/Any/<name>')
def check_name(name):
	sql_qu = "SELECT contactName FROM names WHERE contactName = %s"
	g.mycursor.execute(sql_qu , (name,))
	result = g.mycursor.fetchall()
	if result:
		
		return "True"
	else:
		return "False"


@app.route('/read/<name>')
def read_mysql(name):
	sql_qu = "SELECT contactNumber FROM names WHERE contactName = %s"
	g.mycursor.execute(sql_qu , (name,))
	result = g.mycursor.fetchall()
	if result:
		cache.set(name , result[0][0])
		return	f"{result[0][0]}"
	else:
		return f"False"



if __name__ == '__main__':
      app.run(host='0.0.0.0', port='5005' , debug=True, use_reloader=True)

