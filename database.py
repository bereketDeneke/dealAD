import sqlite3

database = None
database_cursor = None

def open():
    global database
    global database_cursor

    database = sqlite3.connect("postdb.db", uri=True, check_same_thread=False)
    database_cursor = database.cursor()

def close():
    database_cursor.close()
    # database.close()

def INIT():
    open()
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
                                            user_id integer PRIMARY KEY AUTOINCREMENT,
                                            first_name text,
                                            password text,
                                            net_id text
                                        ); """

    database_cursor.execute(create_users_table_query)
    database_cursor.execute(create_buy_table_query)
    database_cursor.execute(create_sell_table_query)
    close()


def getDB():
    return database, database_cursor


def register(username, netid, password):
    open()
    database_cursor.execute("SELECT * FROM users WHERE net_id =?", (netid,))
    user = database_cursor.fetchone()
    print("================================")
    print(user)
    print("================================")
    if user is None:
        database_cursor.execute("INSERT INTO users (first_name, password, net_id) VALUES (?,?,?)",
                                (username, password, netid))
        database.commit()
        close()
        return True
    close()
    return "User already exist"


def login(netid, password):
    open()
    database_cursor.execute("SELECT * FROM users WHERE net_id =? and password=?", (netid, password))
    user = database_cursor.fetchone()

    close()
    # print("================================")
    # print(login(netid, password))
    # print("================================")
    if user is None:
        return False  # the user is not registered
    else:
        return True  # the user logged in successfully


def my_posts(netid):
    open()
    # select the posts
    database_cursor.execute("SELECT * FROM buy_posts WHERE user_name =? ", (netid))
    user = database_cursor.fetchall()

    database_cursor.execute("SELECT * FROM sell_posts WHERE user_name =? ", (netid))
    user += database_cursor.fetchall()

    if user is None:
        close()
        return False  # the user is not registered

    print(user)

    close()
    return user

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