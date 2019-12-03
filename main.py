from flask import Flask, request, redirect, render_template, url_for
import html
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html', ispost = "GET")

@app.route('/', methods=['POST'])
def login():
    if request.method =="POST":

        password = request.form['password']
        username = request.form['username']
        email = request.form['email']
        verify = request.form['verify']
        ispost = request.method
        if len(password) > 3 and len(password) < 20 and ' ' not in password:
            if len(username) > 3 and len(username) < 20 and ' ' not in username:
                if verify == password and verify != '':
                    if email == '' or email.count('@') == 1 and email.count('.') == 1 and len(email) > 3 and len(email) < 20 and ' ' not in email:  
                        return redirect(url_for('welcome'), code=307)
        return render_template('index.html', username=username,password=password, verify=verify, email=email, ispost=ispost)

 

@app.route('/welcome', methods=['POST'])
def welcome():
    username= request.form['username']
    return render_template('welcome.html', username=username)


app.run()