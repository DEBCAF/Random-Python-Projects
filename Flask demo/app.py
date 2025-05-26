#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
import os
import sqlite3 

# Connect to DB. For this to work, sqlite.db must be in the same folder as your .py file!
conn = sqlite3.connect('sqlite.db')

# Create a cursor object - required for running queries on the DB
cursor = conn.cursor()

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__, static_url_path='/static/')
# app.config.from_object('config')

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def home():
    demo_data = {
        'name': 'Dazai Osamu',
        'occupation': 'Author',
        'dob' : '19/06/1909',
        'pob' : 'Japan'
    }
    return render_template('index.html', **demo_data)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/check_login', methods=['POST']) 
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM accounts WHERE email = '"
                + username + "' AND password = '" + password + "'")
    records = cursor.fetchall() # technically, only one record should be returned...

    if len(records) == 0:
        return render_template('login.html', status="login_failed")
    else:
        return render_template('account.html')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''