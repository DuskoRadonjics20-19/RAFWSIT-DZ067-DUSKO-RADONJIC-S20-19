from flask import Flask, render_template, redirect
from flask_mysqldb import MySQL, MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb



app = Flask(__name__)

app.secret_key = "rasporednastave"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'baza'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def main():
    return redirect('raspored')

@app.route('/raspored')
def useradmin():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute("SELECT * FROM raspored")
    raspored = cur.fetchall()
    return render_template('useradmin.html', raspored=raspored)



if __name__ == '__main__':
    app.run(debug=True)


