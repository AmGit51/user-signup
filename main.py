from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('forms.html')

@app.route("/", methods=['POST'])
def validate_entries():

    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    useremail = request.form['useremail']

    username_error = ''
    password_error = ''
    verifypassword_error = ''
    useremail_error = ''
	
    if " " in username or len(username) == 0 or len(username) > 20 or len(username) < 3:
        username_error = 'This is not a vaild username.'

    if " " in password or len(password) == 0 or len(password) > 20 or len(password) < 3:
        password_error = 'This is not a valid password.'
        password = ''

    if " " in verifypassword or len(verifypassword) == 0 or len(verifypassword) > 20 or len(verifypassword) < 3:
        verifypassword_error = 'Re-enter a valid password.'
        verifypassword = ''

    if password != verifypassword:
        if " " in password or len(password) == 0 or len(password) > 20 or len(password) < 3:
            password_error = 'This is not a valid password.'
            password = ''
        elif " " in verifypassword or len(verifypassword) == 0 or len(verifypassword) > 20 or len(verifypassword) < 3:
            verifypassword_error = 'Re-enter a valid password.'
            verifypassword = ''
        else:
            password_error = 'Passwords do not match.'
            verifypassword_error = 'Passwords do not match.'
            password = ''
            verifypassword = ''
  
    if len(useremail) > 1:
        if " " in useremail or len(useremail) > 20 or len(useremail) < 3:
            useremail_error = 'This is not a valid email address.'

        elif "@" not in useremail or "." not in useremail:
            useremail_error = 'This is not a valid email address.'

    if not username_error and not password_error and not verifypassword_error and not useremail_error:
        return render_template('welcome.html', username=username)

    else:

        return render_template('forms.html',
        username = username,
        useremail = useremail,
        username_error = username_error,
        password_error = password_error,
        verifypassword_error = verifypassword_error,
        useremail_error = useremail_error)


app.run()