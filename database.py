import sqlite3

database = None
database_cursor = None

def open():
    global database
    global database_cursor

    database = sqlite3.connect("maindb.db", uri=True, check_same_thread=False)
    database_cursor = database.cursor()

def close():
    database_cursor.close()
    # database.close()

def INIT():
    open()
    create_sell_table_query = """ CREATE TABLE IF NOT EXISTS sell_posts (
                                            post_id integer PRIMARY KEY AUTOINCREMENT,
                                            net_id text,
                                            amount text,
                                            rate text
                                        ); """

    create_buy_table_query = """ CREATE TABLE IF NOT EXISTS buy_posts (
                                            post_id integer PRIMARY KEY AUTOINCREMENT,
                                            net_id text,
                                            amount text,
                                            rate text
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
    user = database_cursor.fetchall()

    close()
    if user is None:
        return False  # the user is not registered
    else:
        return True  # the user logged in successfully


def my_posts(netid):
    open()
    # select the posts
    database_cursor.execute("SELECT * FROM buy_posts WHERE user_id =? ", (netid,))
    user = database_cursor.fetchall()

    database_cursor.execute("SELECT * FROM sell_posts WHERE user_id =? ", (netid,))
    user += database_cursor.fetchall()

    if user is None:
        close()
        return False  # the user is not registered

    close()
    return user

def delete_post(post_id):
    open()
    try:
        database_cursor.execute("DELETE FROM buy_posts WHERE post_id =? ", (post_id,))
        database_cursor.execute("DELETE FROM sell_posts WHERE post_id =? ", (post_id,))
        database.commit()
    except:
        close()
        return False
    close()
    return True

def update_post(offer, exRate, post_id):
    open()
    try:
        database_cursor.execute("UPDATE buy_posts SET amount = ? rate = ? WHERE post_id =? ", (offer, exRate, post_id))
        database_cursor.execute("UPDATE sell_posts SET amount = ? rate = ? WHERE post_id =?", (offer, exRate,post_id))
        database.commit()
    except:
        return False
    close()

####################################################
def create_sell_post(user_id, amount, rate):
    open()
    database_cursor.execute("INSERT INTO sell_posts (net_id, amount, rate) VALUES (?,?,?)",
                            (user_id, amount, rate))
    database.commit()
    close()

def create_buy_post(user_id, amount, rate):
    open()
    database_cursor.execute("INSERT INTO buy_posts (net_id, amount, rate) VALUES (?,?,?)",
                            (user_id, amount, rate))
    database.commit()
    close()

def getSellPosts(sort):
    open()
    if sort == "cheap_first":
        return database_cursor.execute("SELECT * FROM sell_posts ORDER BY rate ASC").fetchall()
    elif sort == "cheap_last":
        return database_cursor.execute("SELECT * FROM sell_posts ORDER BY rate DESC").fetchall()
    else:
        return database_cursor.execute("SELECT * FROM sell_posts ORDER BY post_id DESC").fetchall()


def getBuyPosts(sort):
    open()
    if sort == "cheap_first":
        return database_cursor.execute("SELECT * FROM buy_posts ORDER BY rate ASC").fetchall()
    elif sort == "cheap_last":
        return database_cursor.execute("SELECT * FROM buy_posts ORDER BY rate DESC").fetchall()
    else:
        return database_cursor.execute("SELECT * FROM buy_posts ORDER BY post_id DESC").fetchall()