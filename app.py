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
    amount = request.get("amount")
    rate = request.get("rate")
    print(amount,rate)
    return render_template("posts/create_buy.html")


app.run(debug=True, port=80)

