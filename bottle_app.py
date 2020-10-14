

import os
import sqlite3
from bottle import get, post, template, request, redirect


ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ



if ON_PYTHONANYWHERE:
   
    from bottle import default_app
else:
    
    from bottle import run, debug


@get('/')
def get_show_list():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return template("show_list", rows=result)


@get("/new_item")
def get_new_item():
    return template("new_item")


@post("/new_item")
def post_new_item():
    new_item = request.forms.get("new_item").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("insert into todo (mission, is_active) values (?,?)", (new_item, 1))
    connection.commit()
    cursor.close()
    redirect("/")


@get("/delete_item/<id:int>")
def get_delete_item(id):
    print("we want to delete ", id)
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("delete from todo where id=?", (id,))
    connection.commit()
    cursor.close()
    redirect("/")


@get("/update_item/<id:int>")
def update_new_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo where id=?", (id,))
    result = cursor.fetchall()
    cursor.close()
    return template("update_item", row=result)


@post("/update_item")
def post_new_item():
    updated_item = request.forms.get("updated_item").strip()
    id = request.forms.get("id").strip()
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set mission=? where id=?", (updated_item, id))
    connection.commit()
    cursor.close()
    redirect("/")


@get("/set_is_active/<id:int>/<is_active:int>")
def post_new_item(id, is_active):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set is_active=? where id=?", (is_active, id))
    connection.commit()
    cursor.close()
    redirect("/")


if ON_PYTHONANYWHERE:
  
    application = default_app()
else:
    
    debug(True)
    run(host='localhost', port=8080)


