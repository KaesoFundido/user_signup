from flask import Flask, request
#from templates import 
app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>
<html>
    <body>
        <form method="POST">
        <label></label>
        Username: <input type="text" name="username"/>
        <br>
        Password: <input type="text" name="password"/>
        <br>
        Password Validation: <input type="text" name="validation"/>
        <br>
        Email (optional): <input type="text"/>
        <br>
        <input type="submit" value="Submit">
        </form>
    </body>
</html>

"""
@app.route("/")
def index():
    return form.format('')

@app.route("/welcome")

error_message =="That is not a valid username

def valid-user(username, password, validation):
    if len(username) > 3 and len(username) < 20:
        if character in username != '':
            print ("Welcome, " + username) 
        else:
            return error_message


def 

app.run()