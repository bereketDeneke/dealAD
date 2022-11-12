from database import *
import flask
from flask import render_template, request

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login_tem():
    if request.method == 'POST':
        net_id = request.form['netId']
        password = request.form['password']
        exist = login(net_id, password)

        if exist:
            return render_template('login.html', errorMsg = "")
        else:
            return render_template('login.html', errorMsg=f"The user ,{net_id.capitalize()}, does not exist!!")
    
    return render_template("login.html", errorMsg = "")

@app.route('/register', methods=['GET', 'POST'])
def register_tem():
    
    if request.method == 'POST':
        netId = request.form['net_id']
        password = request.form['password']
        first_name = request.form['first_name']
        confPassword = request.form['conf_password']
        error = ""

        if confPassword != password:
            error = "The password must match!!"
        elif first_name.isalpha():
            error = "All the characters must be an alphabet!!"
        elif netId[0].isdigit():
            error = "The netId must start with alphabet. ie (ab1234)!!"

        is_registered = register(first_name, netId, password)

        if is_registered:
            return render_template('register.html', errorMsg = "")
        else:
            return render_template('register.html', errorMsg=error)
    
    return render_template("register.html", errorMsg="")

@app.route('/my_posts', methods=['GET'])
def myPosts():
    return render_template("posts/my_posts.html")


#  =================================================================
@app.route('/market')
def home():
    sell_posts = getDB.execute("SELECT * FROM sell_posts").fetchall()
    buy_posts = getDB.execute("SELECT * FROM buy_posts").fetchall()
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

