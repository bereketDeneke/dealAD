import sqlite3
import flask
from flask import jsonify, render_template, request

app = flask.Flask(__name__)
DOMAIN = "dealAD"

database = sqlite3.connect("postdb.db", uri=True, check_same_thread=False)
database_cursor = database.cursor()

create_table_query = """ CREATE TABLE IF NOT EXISTS post_table (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        user_name text,
                                        amount integer,
                                        rate integer
                                    ); """
database_cursor.execute(create_table_query)


@app.route('/create', methods=['GET'])
def create_post():
    return render_template("posts/create_post.html")
@app.route('/create/sell', methods=['GET'])
def create_sell():
    return render_template("posts/create_sell.html")

@app.route('/create/sell', methods=['GET', 'POST'])
def create_sell_action():
    if request.method == "POST":
        name = "name" #todo
        amount = request.form.get("amount")
        rate = request.form.get("rate")

        database_cursor.execute(''' INSERT INTO post_table ( user_name, amount, rate )
                       VALUES ( ?, ?,
                       ?); ''', (name, amount, rate))
        database.commit()
        print("Success")
        return render_template("posts/create_sell.html")

@app.route('/create/buy')
def create_buy():
    return render_template("posts/create_buy.html")

@app.route('/create/buy', methods=['GET', 'POST'])
def create_buy_action():
    if request.method == "POST":
        name = "temp"#todo
        amount = request.form.get("amount")
        rate = request.form.get("rate")
        database_cursor.execute(''' INSERT INTO post_table ( user_name, amount, rate )
                               VALUES ( ?, ?,
                               ?); ''', (name, amount, rate))
        database.commit()
        print("Success")
        return render_template("posts/create_buy.html")

# @app.route(f'{DOMAIN}/createSell/', methods=['GET'])
# def getMembers(request):
#     return render_template("createsellPost.html", request)

# @app.route('/api/v1/register', methods=['POST'])
# def register(request):
#     validate.validateInput(request)

app.run(debug=True)



