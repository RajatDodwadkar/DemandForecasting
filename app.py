from flask import Flask, render_template, request, session, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'demand_forecasting'
app.secret_key = os.urandom(24)

mysql = MySQL(app)

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
	return render_template('tools.html')

@app.route("/aboutus")
def aboutus():
	return render_template('aboutus.html')

@app.get('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect('/')

if __name__ == "__main__":
	app.run(debug=True)
