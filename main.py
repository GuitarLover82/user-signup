from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def signup():
    
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    user_name_error = ""
    user_password_error = ""
    verify_password_error = ""
    email_error = ""

    if verify_password == "":
        verify_password_error = "passwords don't match"
        verify_password = ""
        user_password = ""
    elif verify_password != user_password:
        verify_password_error = "passwords don't match"
        verify_password = ""
        user_password = ""

    if user_password == "":
        user_password_error = "That's not a valid password"
        user_password = ""
        verify_password = ""
    elif " " in user_password:
        user_password_error = "That's not a valid password"
        user_password = ""
        verify_password = ""
    elif len(user_password) < 3 or len(user_password) > 20:
        user_password_error = "That's not a valid password"
        user_password = ""
        verify_password = ""

    if user_name == "":
        user_name_error = "That's not a valid user name"
        user_password = ""
        verify_password = ""
    elif " " in user_name:
        user_name_error =  "That's not a valid user name"
        user_password = ""
        verify_password = ""    
    elif len(user_name) < 3 or len(user_name) >20:
        user_name_error = "That's not a valid username"
        user_password = ""
        verify_password = "" 

    if email == "":
        email_error == False
    elif " " in email:
        email_error = "That is not a valid email"
        user_password = ""
        verify_password = ""
    elif "@" not in email or "." not in email:
        email_error = "That is not a valid email"
        user_password = ""
        verify_password = ""
    elif email.count(".") > 1:
        email_error = "That is not a valid email"
        user_password = ""
        verify_password = ""
    elif email.count("@") > 1:
        email_error = "That is not a valid email"
        user_password = ""
        verify_password = ""           
    elif len(email) < 3 or len(email) > 20:
        email_error = "That is not a valid email"
        user_password = ""
        verify_password = ""

    if not user_name_error and not user_password_error and not verify_password_error and not email_error:
        user_name = user_name
        return redirect('/welcome?user_name={0}'.format(user_name))
    else:    
        return render_template('index.html', user_name=user_name, user_name_error=user_name_error, user_password=user_password, 
        user_password_error=user_password_error, verify_password=verify_password, verify_password_error=verify_password_error,
         email=email, email_error=email_error)

@app.route("/welcome")
def welcome():
    user_name = request.args.get('user_name')
    return render_template('welcome.html', user_name=user_name)    

app.run() 