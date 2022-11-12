import flask
from flask import jsonify, render_template, request

app = flask.Flask(__name__)
DOMAIN = "dealAD"

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

# @app.route(f'{DOMAIN}/createSell/', methods=['GET'])
# def getMembers(request):
#     return render_template("createsellPost.html", request)

# @app.route('/api/v1/register', methods=['POST'])
# def register(request):
#     validate.validateInput(request)

app.run(debug=True)



