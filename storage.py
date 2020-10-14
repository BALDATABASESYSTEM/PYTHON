import sqlite3

def get_items():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return result

def get_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo where id=?",(id,))
    result = cursor.fetchall()
    cursor.close()
    return result[0]

def update_is_active(id, value):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set is_active=? where id=?",(value, id))
    connection.commit()
    cursor.close()

def create_item(mission, is_active):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("insert into todo (mission, is_active) values (?,?)", (mission, is_active))
    id = cursor.lastrowid
    connection.commit()
    cursor.close()
    return id

def update_item(id, updated_mission):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set mission=? where id=?", (updated_mission, id))
    connection.commit()
    cursor.close()

def delete_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("delete from todo where id=?", (id,))
    connection.commit()
    cursor.close()

def test_get_items():
    print("testing get_items")
    results = get_items()
    assert type(results) is list
    assert len(results) > 0
    for item in results:
        assert type(item) is tuple
    id, mission, is_active = results[0]
    assert type(id) is int
    assert type(mission) is str
    assert type(is_active) is int
    assert is_active in [0,1]

def test_get_item():
    print("testing get_item(id)")
    results = get_items()
    assert len(results) > 0
    id, mission, is_active = results[0]
    result = get_item(id)
    assert type(result) is tuple
    id2, mission2, is_active2 = result
    assert id2 == id
    assert mission2 == mission
    assert is_active2 == is_active

if __name__ == "__main__":
    
    test_get_item()
    print("done.")

