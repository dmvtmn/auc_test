# blog.py - controller

# imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3
from functools import wraps

# configuration
DATABASE = 'offre.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

# pulls in configurations by looking for UPPERCASE variables
app.config.from_object(__name__)


# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/main')
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute('select * from ubscores')
    points = [dict(ub=row[0], score_saturation=row[1], score_performance=row[2], score_loyalty=row[3], score_dynamisme = row[4], score_final = row[5]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html', points = points)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
@login_required
def add():
    ub = request.form['ub']
    score_saturation = int(request.form['score_saturation'])
    score_performance = int(request.form['score_performance'])
    score_loyalty = int(request.form['score_loyalty'])
    score_dynamisme = int(request.form['score_dynamisme'])
    score_final = request.form['score_final']

    if not ub or not score_saturation or not score_performance or not score_loyalty or not score_dynamisme or not score_final :
        flash("Merci de renseigner toutes les infos")
        return redirect(url_for('main'))
    else:
        g.db = connect_db()
        g.db.execute(
            'insert into ubscores (ub, score_saturation,score_performance, score_loyalty, score_dynamisme, score_final) values (?,?,?,?,?,?)',
            [request.form['ub'], request.form['score_saturation'], request.form['score_performance'], request.form['score_loyalty'], request.form['score_dynamisme'], request.form['score_final']]
            )
        g.db.commit()
        g.db.close()
        flash('Nouvelle data point bien enregistre')
        return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)
