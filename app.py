from flask import Flask, render_template,request
from flask_app.models import init_db,self_user,check_user

app = Flask(__name__)
app.secret_key = 'secret123'

#initialize database
init_db()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username=request.form.get('username')
    password=request.form.get('password')

    self_user(username,password)
    return render_template('index.html',message="User Registration Successful")  

@app.route('/login', methods=['POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')

    if check_user(username,password):
        return render_template('login.html',message="Login Successful")
    else:
        return render_template('login.html',message="Invalid Credentials")

@app.route('/login.page')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)