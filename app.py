import sqlite3
import flask
from flask import jsonify, render_template, request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    return render_template("login.html")

@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")

@app.route('/my_posts', methods=['GET'])
def myPosts():
    return render_template("posts/my_posts.html")

database = sqlite3.connect("postdb.db", uri=True, check_same_thread=False)
database_cursor = database.cursor()

create_sell_table_query = """ CREATE TABLE IF NOT EXISTS sell_posts (
                                        post_id integer PRIMARY KEY AUTOINCREMENT,
                                        user_id integer,
                                        amount integer,
                                        rate integer
                                    ); """

create_buy_table_query = """ CREATE TABLE IF NOT EXISTS buy_posts (
                                        post_id integer PRIMARY KEY AUTOINCREMENT,
                                        user_id integer,
                                        amount integer,
                                        rate integer
                                    ); """

create_users_table_query = """ CREATE TABLE IF NOT EXISTS users (
                                        userid integer PRIMARY KEY AUTOINCREMENT,
                                        firstname text,
                                        password text,
                                        netid text
                                    ); """

database_cursor.execute(create_users_table_query)
database_cursor.execute(create_buy_table_query)
database_cursor.execute(create_sell_table_query)

@app.route('/')
def home():
    sell_posts = database_cursor.execute("SELECT * FROM sell_posts").fetchall()
    buy_posts = database_cursor.execute("SELECT * FROM buy_posts").fetchall()
    return render_template("posts/browse.html", sell_posts=sell_posts, buy_posts=buy_posts)

@app.route('/create', methods=['GET'])
def create_post():
    return render_template("posts/create_post.html")
@app.route('/create/sell', methods=['GET'])
def create_sell():
    return render_template("posts/create_sell.html")

@app.route('/create/sell', methods=['GET', 'POST'])
def create_sell_action():
    return render_template("posts/create_sell.html")
@app.route('/create/buy', methods=['GET'])
def create_buy():
    return render_template("posts/create_buy.html")

@app.route('/create/buy', methods=['GET', 'POST'])
def create_buy_action():
    if request.method == "POST":
        name = "temp"#todo
        amount = request.form.get("amount")
        rate = request.form.get("rate")
        database_cursor.execute(''' INSERT INTO buy_posts ( user_name, amount, rate )
                               VALUES ( ?, ?,
                               ?); ''', (name, amount, rate))
        database.commit()
        return render_template("posts/create_buy.html")


app.run(debug=True, port=80)

