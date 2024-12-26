from flask import Flask, render_template


app = Flask(__name__, template_folder="../client/templates")

@app.route("/")
def create_login_page():
    return render_template("login.html")

@app.route("/register")
def create_registration():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)