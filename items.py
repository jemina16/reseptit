import db

def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes

def add_item(title, description, user_id, classes):
    sql = """INSERT INTO items (title, description, user_id) VALUES (?, ?, ?)"""
    db.execute(sql, [title, description, user_id])

    item_id = db.last_insert_id()

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for class_title, class_value in classes:
        db.execute(sql, [item_id, class_title, class_value])

def add_comment(item_id, user_id, note):
    sql = """INSERT INTO comments (item_id, user_id, note) VALUES (?, ?, ?)"""
    db.execute(sql, [item_id, user_id, note])

def get_comments(item_id):
    sql = """SELECT comments.note, users.id user_id, users.username
             FROM comments, users
             WHERE comments.item_id = ? AND comments.user_id = users.id
             ORDER BY comments.id DESC"""
    return db.query(sql, [item_id])

def get_images(item_id):
    sql = "SELECT id FROM images WHERE item_id = ?"
    return db.query(sql, [item_id])

def add_image(item_id, image):
    sql = "INSERT INTO images (item_id, image) VALUES (?, ?)"
    db.execute(sql, [item_id, image])

def get_image(image_id):
    sql = "SELECT image FROM images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def remove_images(item_id, image_id):
    sql = "DELETE FROM images WHERE id = ? AND item_id = ?"
    db.execute(sql, [image_id, item_id])

def get_classes(item_id):
    sql = "SELECT title, value FROM item_classes WHERE item_id = ?"
    return db.query(sql, [item_id])

def get_items():
    sql = """SELECT items.id, items.title, users.id user_id, users.username,
                    COUNT(comments.id) comment_count
             FROM items JOIN users ON items.user_id = users.id
                        LEFT JOIN comments ON items.id = comments.item_id
             GROUP BY items.id
             ORDER BY items.id DESC"""
    return db.query(sql)

def get_item(item_id):
    sql = """SELECT items.id,
                    items.title,
                    items.description,
                    users.id user_id,
                    users.username
            FROM items, users
            WHERE items.user_id = users.id AND
                  items.id = ?"""
    result = db.query(sql, [item_id])
    return result[0] if result else None

def update_item(item_id, title, description, classes):
    sql = """UPDATE items SET title = ?,
                              description = ?
                          WHERE id = ?"""
    db.execute(sql, [title, description, item_id])

    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "INSERT INTO item_classes (item_id, title, value) VALUES (?, ?, ?)"
    for class_title, class_value in classes:
        db.execute(sql, [item_id, class_title, class_value])

def remove_item(item_id):
    sql = "DELETE FROM item_classes WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "DELETE FROM images WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "DELETE FROM comments WHERE item_id = ?"
    db.execute(sql, [item_id])

    sql = "DELETE FROM items WHERE id = ?"
    db.execute(sql, [item_id])

def find_items(query):
    sql = """SELECT id, title
             FROM items
             WHERE title LIKE ? OR description LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])
