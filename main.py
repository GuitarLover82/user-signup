from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST', 'GET'])
def index():
    template = jinja_env.get_template('index.html')
    return template.render()



@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    template = jinja_env.get_template('welcome.html')
    
    user_name = request.form['user_name']
    user_password = request.form['user_password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    user_name_error = ""
    user_password_error = ""
    verify_password_error = ""
    email_error = ""

    if user_name == "":
        user_name_error = "That's not a valid user name"
    elif " " in user_name:
        user_name_error =  "That's not a valid user name"    
    elif len(user_name) < 3 or len(user_name) >20:
        user_name_error = "That's not a valid username" 

    if user_password == "":
        user_password_error = "That's not a valid password"
    elif " " in user_password:
        user_password_error = "That's not a valid password"
    elif len(user_password) < 3 or len(user_password) > 20:
        user_password_error = "That's not a valid password"
        user_password = ""

    if verify_password == "":
        verify_password_error = "passwords don't match"
    elif verify_password != user_password:
        verify_password_error = "passwords don't match"
        verify_password = ""

    if " " in email:
        email_error = "That is not a valid email"
    elif "@" not in email or "." not in email:
        email_error = "That is not a valid email"
    elif len(email) < 3 or len(email) > 20:
        email_error = "That is not a valid email"

    if not user_name_error and not user_password_error and not verify_password_error and not email_error:
        return 
    else:    
        return template.render(user_name=user_name, user_name_error=user_name_error, user_password=user_password, 
        user_password_error=user_password_error, verify_password=verify_password, verify_password_error=verify_password_error,
         email=email, email_error=email_error)

app.run() 