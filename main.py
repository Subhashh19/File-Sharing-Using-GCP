from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html", title="HOME PAGE")

@app.route("/register")
def register():
    return render_template("register.html", title="register page")

@app.route("/share")
def share():
    return render_template("share.html", title="share page")

if __name__ == "__main__":
    app.run(debug=True)