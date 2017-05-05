import os
import sqlite3
from behave import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr_test.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

os.environ['FLASK_APP'] = 'flaskr' # to avoid error msg


def connect_db():
    """ Connect to database """
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
    #if app.environment == 'test':
    #    os.unlink(app.config['DATABASE') # can't delete here


def init_db(schema='schema.sql'):
    db = get_db()
    with app.open_resource(schema, mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.route('/')
def show_entries():
    return render_template('show_entries.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
            db = get_db()
            cur = db.execute("select username from users")
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            password1 = request.form['password1']
            print (username)
            if password != password1:
                flash("Please confirm your password")
                return render_template('registration.html', error=error)
            else:
                rows = cur.fetchone()
                if username in rows:
                    flash("User name has already existed, please try again")
                    return render_template('registration.html', error=error)
                elif len(username) > 10 or len(username) < 4 or len(password) != 8:
                    flash("Username or password invalid")
                    return render_template('registration.html', error=error)
                else:
                    flag1 = 0
                    flag2 = 0
                    flag3 = 0
                    for i in password:
                        if i.isdigit():
                            flag1 = 1
                        elif i.islower():
                            flag2 = 1
                        elif i.isupper():
                            flag3 = 1
                    if flag1 == 1 and flag2 == 1 and flag3 == 1:
                        db.execute('insert into users (username, email,password) values (?,?, ?)',
                        (username,email, password))
                        db.commit()
                        flash('Register successfully')
                        return redirect(url_for('show_entries'))
                    else:
                        flash("Username or password invalid")
                        return render_template('registration.html', error=error)
    return render_template('registration.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
        error = None
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if username and password:
                db = get_db()
                cur = db.execute("select *  from users where username =? and password=?", [username, password])
                rows = cur.fetchone()
                cur1 = db.execute("select *  from users where Email =? and password=?", [username, password])
                rows1 = cur1.fetchone()
                if rows or rows1:
                    session['logged_in'] = True
                    flash("Login Success!")
                else:
                    error = "Bad Login"
            else:
                error = "Missing user credentials"
        return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


def serve_forever():
    app.run()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    if app.environment == 'test':
        func()
        os.unlink(app.config['DATABASE'])


@app.route('/shutdown')
def shutdown():
    if app.environment == 'test':
        shutdown_server()
    return "Server shutdown"


@app.cli.command('start')
def start():
    app.config.from_object(__name__) # load config from this file

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr_test.db'),
        SECRET_KEY='Production key',
    ))
    app.config.from_envvar('FLASKR_SETTINGS',  silent=True)

    app.run()


def test_server():
    ### Setup for integration testing
    app.config.from_object(__name__) # load config from this file

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr_test.db'),
        SECRET_KEY='Test key',
        SERVER_NAME='localhost:5000',
        Login_NAME='localhost/login:5000',
        # DEBUG=True, # does not work from behave
    ))
    app.environment = 'test'
    with app.app_context():
        init_db('test_schema.sql')
    app.run()

if __name__ == '__main__':
        app.run()




