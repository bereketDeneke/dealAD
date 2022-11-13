from database import *
import flask
from flask import render_template, request,session, make_response, redirect, json, Response

app = flask.Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'hekls%%^$##GHB'

@app.route('/', methods=['GET','POST'])
def login_tem():
    if request.method == 'POST':
        net_id = request.form['net_id']
        password = request.form['password']

        if len(net_id) <= 4 or len(password) <= 0:
            return render_template("login.html", errorMsg="")

        exist = login(net_id, password)

        if exist:
            session["netId"] = net_id
            session["password"] = password
            return market_buy()
        else:
            return render_template('login.html', errorMsg=f"The user ,{net_id.capitalize()}, does not exist!!")
    
    return render_template("login.html", errorMsg = "")


@app.route('/register', methods=['GET','POST'])
def register_tem():  
    if request.method == 'POST':
        netId = request.form['net_id']
        password = request.form['password']
        first_name = request.form['first_name']
        confPassword = request.form['conf_password']
        error = ""

        if len(netId) <= 4 or len(password) <= 0:
            return render_template("register.html", errorMsg="")

        if confPassword != password:
            error = "The password must match!!"
        elif first_name.isalpha():
            error = "All the characters must be an alphabet!!"
        elif netId[0].isdigit():
            error = "The netId must start with alphabet. ie (ab1234)!!"

        is_registered = register(first_name, netId, password)

        if is_registered:
            return login_tem()
        else:
            return render_template('register.html', errorMsg=error)
    
    return render_template("register.html", errorMsg="")

@app.route('/my_posts', methods=['GET', 'POST'])
def myPosts():    
    if not session.get("netId"):
        return login_tem()

    username = session.get('netId')
    password = session.get('password')

    exist = login(username, password)
    if exist:
        posts = my_posts(username)
        print(username)
        return render_template("posts/my_posts.html", posts=posts)
    else:
        return redirect("./")

@app.route('/api/v1/update/', methods=['POST'])
def update_post_tem():
    data = json.loads(request.data)
    offer = data['offer']
    rate = data['rate']
    postId = data['postId']
    return update_post(offer,rate,postId)


@app.route('/api/v1/decline/', methods=['POST'])
def delete_post_tem():
    data = json.loads(request.data)
    postId = data['postId']
    return delete_post(postId)

#  =================================================================
INIT()

@app.route('/market/buy')
def market_buy():
    sort = request.args.get('sort')
    buy_posts = getBuyPosts(sort)

    if not session.get("netId"):
        return redirect('./')

    username = session.get('netId')
    password = session.get('password')

    if buy_posts is None:
        buy_posts = []

    if login(username, password):
        return render_template("posts/browse_buy.html", buy_posts=buy_posts)
    else:
        return redirect('./')

@app.route('/market/sell')
def market_sell():
    sort = request.args.get('sort')
    sell_posts = getSellPosts(sort)

    if not session.get("netId"):
        return redirect('./')

    username = session.get('netId')
    password = session.get('password')

    if sell_posts is None:
        sell_posts = []

    if login(username, password):
        return render_template("posts/browse_sell.html", sell_posts=sell_posts)
    else:
        return redirect('./')

@app.route('/create', methods=['GET'])
def create_post():
    
    if not session.get("netId"):
        return redirect('./')

    username = session.get('netId')
    password = session.get('password')
    if login(username, password):
        return render_template("posts/create_post.html")
    else:
        return login_tem()

@app.route('/create/sell', methods=['GET'])
def create_sell():
    if not session.get("netId"):
        return redirect('./')

    username = session.get('netId')
    password = session.get('password')
    if login(username, password):
        return render_template("posts/create_sell.html")
    else:
        return login_tem()


@app.route('/create/sell', methods=['GET', 'POST'])
def create_sell_action():
    if request.method == "POST":
        user_id = "1234"  # todo
        amount = request.form.get("amount")
        rate = request.form.get("rate")
        create_sell_post(user_id, amount, rate)
        return render_template("posts/create_sell.html")
    return render_template("posts/create_sell.html")

@app.route('/create/buy', methods=['GET'])
def create_buy():
    return render_template("posts/create_buy.html")


@app.route('/create/buy', methods=['GET', 'POST'])
def create_buy_action():
    if request.method == "POST":
        user_id = "1234"  # todo
        amount = request.form.get("amount")
        rate = request.form.get("rate")
        create_buy_post(user_id, amount, rate)
        return render_template("posts/create_buy.html")
    return render_template("posts/create_buy.html")

app.run(debug=True)