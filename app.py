from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials
USER_ID = "admin"
PASSWORD = "password"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':     
        user_id = request.form['userid']
        password = request.form['password']
        if user_id == USER_ID and password == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials, please try again."

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/page/<page_no>')
def render_page(page_no):
    try:
        return render_template(f'{page_no}.html')
    except:
        return "Page not found."

if __name__ == '__main__':
    app.run(debug=True)