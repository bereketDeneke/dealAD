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



