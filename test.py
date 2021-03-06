from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route("/test")
def home():
	return"hello main page <h1> big<h1>"

@app.route("/<name>")
def user(name):
	return f"Hello {name}!"

@app.route("/admin")
def admin():
	return redirect(url_for("home"))


if __name__ == "__main__":
	app.run()
