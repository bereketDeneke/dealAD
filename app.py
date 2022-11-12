from database import *
import flask
from flask import jsonify, render_template, request

app = flask.Flask(__name__)

INIT()
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
@app.route('/market/buy')
def market_buy():
    buy_posts = getDB()[1].execute("SELECT * FROM buy_posts").fetchall()
    return render_template("posts/browse_buy.html", buy_posts=buy_posts)

@app.route('/market/sell')
def market_sell():
    sell_posts = getDB()[1].execute("SELECT * FROM sell_posts").fetchall()
    return render_template("posts/browse_sell.html", sell_posts=sell_posts)

@app.route('/create', methods=['GET'])
def create_post():
    return render_template("posts/create_post.html")

@app.route('/create/sell', methods=['GET'])
def create_sell():
    return render_template("posts/create_sell.html")

@app.route('/create/sell', methods=['GET', 'POST'])
def create_sell_action():
    if request.method == "POST":
        user_name = "ay2395"
        amount = request.form.get("amount")
        rate = request.form.get("rate")
        getDB()[0].execute(''' INSERT INTO sell_posts ( user_name, amount, rate )
                               VALUES ( ?, ?,
                               ?); ''', (user_name, amount, rate))
        getDB()[1].commit()
        return render_template("posts/create_sell.html")
    return render_template("posts/create_sell.html")

@app.route('/create/buy', methods=['GET'])
def create_buy():
    return render_template("posts/create_buy.html")

@app.route('/create/buy', methods=['GET', 'POST'])
def create_buy_action():
    if request.method == "POST":
        user_name = "temp"#todo
        amount = request.form.get("amount")
        rate = request.form.get("rate")
        getDB()[1].execute(''' INSERT INTO buy_posts ( user_name, amount, rate )
                               VALUES ( ?, ?,
                               ?); ''', (user_name, amount, rate))
        getDB()[0].commit()
        return render_template("posts/create_buy.html")
    return render_template("posts/create_sell.html")

app.run(debug=True)

