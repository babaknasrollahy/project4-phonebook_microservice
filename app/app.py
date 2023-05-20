from flask import Flask , render_template, request
import redis
import requests

cache = redis.Redis(host='localhost' , port=6379 , db=0)

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template("index.html")



@app.route('/create/')
def create():
	return render_template("create_page.html")


@app.route('/read/')
def read():
	return render_template("read_page.html")



@app.route('/create_data/' , methods=['POST'])
def create_data():
	name = request.form.get('name')
	number = request.form.get('number')
	val = cache.get(name)
	if val == None :
		if requests.get(f'http://localhost:5005/api/Any/{name}').text == "True" :
			return "your contact is already exist"
		cache.set(name,number)
		requests.get(f'http://localhost:5005/{name}')
		return f"your contact added :))"

	#return f"name is {name} , num is {number} , val is {val}"
	else:

		print(f"{val} in else")
		return "this name is already difined!!"

@app.route('/read_data/', methods=['POST'])
def read_data():
	name = request.form.get('name')
	val = cache.get(name)
	if val == None :
		mysql_result = requests.get(f'http://localhost:5005/read/{name}')

		if mysql_result.text == "False":
			return f"{name} is not exist"
		else:
			return f"{name}		{mysql_result.text}"

	else:
		val = int(val)
		return f"{name}       {val}"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80 , debug=True, use_reloader=True)
