from flask import Flask, request, session, redirect, url_for, render_template
from flask_keyauth import KeyAuthAPI

app = Flask(__name__)
app.secret_key = 'another_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        api = KeyAuthAPI('your_app_name', 'your_owner_id')
        api.init()
        result = api.login(username, password)
        if result:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error=result)
    if 'user_data' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        key = request.form['key']
        api = KeyAuthAPI('your_app_name', 'your_owner_id')
        api.init()
        result = api.register(username, password, key)
        if result:
            return redirect(url_for('dashboard'))
        else:
            return render_template('register.html', error=result)
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_data' in session:
        user_data = session['user_data']
        username = user_data.get('username')
        subscriptions = user_data.get('subscriptions')
        subscription = subscriptions[0].get('subscription') if subscriptions else None
        expiry = subscriptions[0].get('expiry') if subscriptions else None
        ip = user_data.get('ip')
        creationDate = user_data.get('createdate')
        lastLogin = user_data.get('lastlogin')
        
        return render_template('dashboard.html', username=username, subscriptions=subscriptions,
                               subscription=subscription, expiry=expiry, ip=ip,
                               creationDate=creationDate, lastLogin=lastLogin)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)