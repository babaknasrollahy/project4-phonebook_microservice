from flask import Flask , render_template, request
import redis

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
		cache.set(name,number)
		print(f"{val} in if , name is {name} , num is {number} ")
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
		return f"contact '{name}' undifined"

	else:
		val = int(val)
		return f"{name}       {val}"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80 , debug=True, use_reloader=True)
