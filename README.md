# Flask KeyAuth

A simple Flask extension to integrate KeyAuth API.

## Installation

```bash
git clone https://github.com/Sorted1/flask-keyauth.git
cd flask-keyauth
python setup.py install
```
## Usage/Examples

```python
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
        return render_template('dashboard.html', user_data=session['user_data'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
```
## Contributing

Contributions are welcome! Please submit a pull request or open an issue on GitHub.
## Authors

- [@Sorted1](https://www.github.com/sorted1)

