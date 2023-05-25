from flask import Flask, render_template
import sqlite3
import os
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

app = Flask(__name__)

#config
sfile = ConfigParser()
sfile.read('save.ini')

DATABASE = 'flsite.db'
DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY")
USERNAME = 'admin'
PASSWORD = '1234'

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


#create_db()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/games')
def index():
    return render_template('index.html')


@app.route('/snake')
def snake():
    return render_template('games/snake.html')


@app.route('/tictactoe')
def tictactoe():
    return render_template('games/tictactoe.html')


@app.route('/flappybug')
def flappybug():
    return render_template('games/flappybug/index.html')


@app.route('/crosstheroad')
def crosstheroad():
    return render_template('games/crosstheroad.html')


clickredvar = sfile.getint('colorclicker', 'red')
clickbluevar = sfile.getint('colorclicker', 'blue')

# sfile.set('colorclicker', 'red', str(0))
# sfile.set('colorclicker', 'blue', str(0))

# with open('save.ini', 'w') as configfile:
#         sfile.write(configfile)


@app.route('/colorclicker')
def colorclicker():
    return render_template('games/colorclicker/base.html',
                           red=clickredvar,
                           blue=clickbluevar)


@app.route('/colorclicker/clickred', methods=['GET', 'POST'])
def clickred():
    global clickredvar
    clickredvar += 1
    sfile.set('colorclicker', 'red', str(clickredvar))
    print(clickredvar)
    with open('save.ini', 'w') as configfile:
        sfile.write(configfile)
    return ''


@app.route('/colorclicker/clickblue', methods=['GET', 'POST'])
def clickblue():
    global clickbluevar
    clickbluevar += 1
    sfile.set('colorclicker', 'blue', str(clickbluevar))
    print(clickbluevar)
    with open('save.ini', 'w') as configfile:
        sfile.write(configfile)
    return ''


@app.route('/colorclicker/getred', methods=['GET', 'POST'])
def getred():
    return render_template('games/colorclicker/red.html', red=clickredvar)


@app.route('/colorclicker/getblue', methods=['GET', 'POST'])
def getblue():
    return render_template('games/colorclicker/blue.html', blue=clickbluevar)


@app.route('/arkanoid')
def arkanoid():
    return render_template('games/arkanoid.html')


@app.route('/parkingsimulator')
def parkingsim():
    return render_template('games/parkingsimulator.html')


@app.route('/wordle')
def wordle():
    return render_template('games/wordle.html')


@app.route("/tower")
def tower():
    return render_template('games/tower.html')


#courses

app.run(host='0.0.0.0', port=81)
