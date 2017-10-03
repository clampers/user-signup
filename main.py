from flask import Flask, request, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['GET','POST'])
def validate_userdata():
    error = ''
    username = request.form['username']
    password = request.form['password']
    verify-password = request.form['verify-password']
    fav-food = request.form['fav-food']

    if username == (''):
        error = "Please enter a username."
        return error
    if (' ') in username:
        error = "Usernames cannot contain spaces"
        return error

    return render_template('user-login.html')

app.run()