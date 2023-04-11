from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('auth/login.html')

@app.route('/signup')
def signup():
	return render_template('auth/signup.html')

@app.route('/tools')
def tools():
	return render_template('tools.html')

@app.route("/aboutus")
def aboutus():
	return render_template('aboutus.html')

if __name__ == "__main__":
	app.run(debug=True)
