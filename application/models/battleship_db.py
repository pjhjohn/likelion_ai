import pymysql
from flask import g

def get_db():
    if not hasattr(g,'db'):
        g.db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='likelion', db='battleship_new')
        cur = g.db.cursor()
        cur.execute('SET NAMES utf8')
    return g.db

def execute(query):
    db = get_db()
    cur = db.cursor(pymysql.cursors.DictCursor)
    cur.execute(query)
    return cur

def insert(query):
    cur = execute(query)
    get_db().commit()
    return cur

def select(query):
    cur = execute(query)
    return cur.fetchall()

def count(query):
    return execute(query).rowcount

def escape(data):
    return get_db().escape(data)
