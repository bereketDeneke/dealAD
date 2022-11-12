from database import *
import flask
from flask import jsonify, render_template, request

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def login():
    if request.method == 'POST':
        netId = request['netid']
        password = request['password']
        
    return render_template("login.html")

@app.route('/register', methods=['GET'])
def register():
    return render_template("register.html")

@app.route('/my_posts', methods=['GET'])
def myPosts():
    return render_template("posts/my_posts.html")


#  =================================================================
@app.route('/market')
def home():
    sell_posts = getDB.execute("SELECT * FROM sell_posts").fetchall()
    buy_posts = getDB.execute("SELECT * FROM, buy_posts").fetchall()
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

