# Questions for class: How do I return seperate errors when rendering my template?
# How do I make user input persist through attempted form submission? The example does not do this.

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/signup', methods=['GET','POST'])
def validate_userdata():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    usernameerror = ''
    passworderror = ''
    verifyerror = ''
    emailerror = ''

    if username == ('') or (not username) or (username.strip() == ''):
        usernameerror = "Please enter a username"
    elif ' ' in username:
        usernameerror = "Usernames cannot contain spaces"
    elif len(username) < 3 or len(username) > 19:
        usernameerror = "Usernames must be at least 3 characters and fewer than 20"

    if password == ('') or (not password) or (password.strip() == ''):
        passworderror = "Please enter a password"
    elif ' ' in password:
        passworderror = "Passwords cannot contain spaces"
    elif len(password) < 3 or len(password) > 19:
        passworderror = "Passwords must be at least 3 characters and fewer than 20"
    
    if verify != password or verify == '' or " " in verify:
        verifyerror = "Passwords do not match"

    if email.count("@") != 1 and email.count(".") != 1:
        emailerror = "Invalid email"
        
    
    if (usernameerror != '') or (passworderror != '') or (verifyerror != '') or (emailerror != ''):
        return render_template("signup.html", usernameerror=usernameerror, passworderror=passworderror,
        verifyerror=verifyerror, emailerror=emailerror, username=username, email=email)

    else:
        return render_template("welcome.html", username=username)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("signup.html")

app.run()