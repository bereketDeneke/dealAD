import sqlite3

database = sqlite3.connect("postdb.db", uri=True, check_same_thread=False)
database_cursor = database.cursor()


def INIT():
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


def getDB():
    return database, database_cursor


def register(username, netid, password):
    database_cursor.execute("SELECT * FROM users WHERE netid =? or", (netid,))
    user = database_cursor.fetchone()

    if user is None:
        database_cursor.execute("INSERT INTO users (firstname, password, netid) VALUES (?,?,?)",
                                (username, password, netid))
    else:
        return "User already exist"


def login(netid, password):
    database_cursor.execute("SELECT * FROM users WHERE netid =? and password=?", (netid, password))
    user = database_cursor.fetchone()

    if user is None:
        return False  # the user is not registered
    else:
        return True  # the user logged in successfully


def my_posts(request):
    username = request.GET['username']
    netid = request.GET['netid']
    password = request.GET['password']

    if not login(netid, password):
        return False  # the user is not logged in

    # select the posts
    database_cursor.execute("SELECT * FROM buy_posts WHERE user_name =? ", (netid))
    user = database_cursor.fetchall()

    database_cursor.execute("SELECT * FROM sell_posts WHERE user_name =? ", (netid))
    user += database_cursor.fetchall()

    if user is None:
        return False  # the user is not registered

    print(user)

####################################################

def create_sell_post(user_id, amount, rate):
    database_cursor.execute("INSERT INTO sell_posts (user_id, amount, rate) VALUES (?,?,?)",
                            (user_id, amount, rate))
    database.commit()

def create_buy_post(user_id, amount, rate):
    database_cursor.execute("INSERT INTO buy_posts (user_id, amount, rate) VALUES (?,?,?)",
                            (user_id, amount, rate))
    database.commit()
def getSellPosts():
    return database_cursor.execute("SELECT * FROM sell_posts").fetchall()


def getBuyPosts():
    return database_cursor.execute("SELECT * FROM buy_posts").fetchall()