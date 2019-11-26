from flask import Flask, request, render_template
import html






app = Flask(__name__)
app.config['DEBUG'] = True

form = """



"""
@app.route("/")
def index():
    return render_template("index.html", username="", email="", error_type="", error_message="")
@app.route("/", methods=['POST'])
def login():
    if request.form["password"] =="":
        return render_template("index.html", username= request.form['username'], email= request.form['email'], error_type="bad_password", error_message="This is an invalid password")
    else:
        return render_template("welcome.html")

@app.route("/welcome")


def valid_user(username, password, validation):
    return render.template("welcome.html")


#hello flask and time validation code!
app.run()