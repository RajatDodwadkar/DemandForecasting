from flask import Flask, render_template, request, session, redirect, jsonify
from flask_mysqldb import MySQL
import os
from utils import prediction

app = Flask(__name__)

# Disable File Caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'demand_forecasting'
app.secret_key = os.urandom(24)

mysql = MySQL(app)

@app.after_request
def add_header(r):
	"""
	Add headers to both force latest IE rendering engine or Chrome Frame,
	and also to cache the rendered page for 10 minutes.
	"""
	r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
	r.headers["Pragma"] = "no-cache"
	r.headers["Expires"] = "0"
	r.headers['Cache-Control'] = 'public, max-age=0'
	return r

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if 'logged_in' in session:
		return redirect('/')
	
	if request.method == "POST":
		email = request.form['email']
		password = request.form['password']
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM user WHERE email = '%s' AND password = '%s'" % (email,password))
		user = cur.fetchone()
		if user:
			session['logged_in'] = True
			return redirect('/')
		else:
			return render_template('auth/login.html', msg='Invalid username or password')

	return render_template('auth/login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if 'logged_in' in session:
		return redirect('/')

	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM user WHERE email = '%s'" % (email))
		user = cur.fetchone()
		if user:
			return render_template('auth/signup.html', msg="Email already registered!")
		cur.execute("INSERT INTO user (email, password) VALUES ('%s', '%s')" % (email, password))
		mysql.connection.commit()
		session['logged_in'] = True
		return redirect('/')

	return render_template('auth/signup.html')

@app.route('/tools')
def tools():
	if 'logged_in' not in session:
		return redirect('/login')
	variable = request.args.get('medicine')
	country = request.args.get('country')
	if variable and country:
		sale_prediction = prediction.predict(variable, country)
		return render_template('results.html', predict=sale_prediction)
	elif variable:
		return render_template('tools.html', variables=prediction.variables, countrys=prediction.get_countrys(variable))
	return render_template('tools.html', variables=prediction.variables)

@app.route("/aboutus")
def aboutus():
	return render_template('aboutus.html')

@app.get('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)
