from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    username = request.form['username']
    password = request.form['password']
    vp = request.form['verify-password']
    email = request.form['email']
    food = request.form['fav-food']
    usernamerror = ''
    passworderror = ''
    emailerror = ''

    if username == ('') or (not username) or (username.strip() == "") :
        usernameerror = "Please enter a username"
        return redirect("/?error=" + usernameerror)
    if ' ' in username:
        usernameerror = "Usernames cannot contain spaces"
        return redirect("/?error=" + usernameerror)
    if len(username) < 3 or len(username) > 19:
        usernameerror = "Usernames must be at least 3 characters and fewer than 20"
        return redirect("/?error=" + usernameerror)
    # if password == ('') or (not password) or (username.strip() == "") :
    #     passworderror = "Please enter a password"
    #     return redirect("/?error=" + passworderror)

    return render_template('welcome.html', username=username)

@app.route('/')
def validate_userdata():
    encoded_error = request.args.get("error")
    return render_template('user-login.html', error=encoded_error)

app.run()