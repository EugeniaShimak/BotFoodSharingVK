import pymysql.cursors
import json


# соединение с БД
def get_connection():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='db_bot',
                           cursorclass=pymysql.cursors.DictCursor)

    return conn


# добавить пользователя с выбранной категорией и локацией
def add_to_users(id_user, id_cat, loc):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO users (id_user, id_category, location) VALUES (%s, %s, %s)'
        cursor.execute(sql, (id_user, id_cat, loc))
        conn.commit()
    finally:
        conn.close()
    print("Success")


# получить список категорий и локаций одного пользователя или всех
def get_from_users(id_user=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        if id_user is None:
            sql = 'SELECT u.id_user, c.name, u.location FROM users u, categories c ' + \
                  'WHERE c.id = u.id_category'
            cursor.execute(sql)
        else:
            sql = 'SELECT u.id_user, c.name, u.location FROM users u, categories c ' + \
                  'WHERE u.id_user = %s AND c.id = u.id_category'
            cursor.execute(sql, (id_user,))
        # print(cursor.description)
        result = []
        for row in cursor:
            result.append(row)
    finally:
        conn.close()
    return result


# получить все категории
def get_categories():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'SELECT id, name FROM categories ORDER BY id'
        cursor.execute(sql)
        result = []
        for row in cursor:
            result.append(row)
    finally:
        conn.close()
    return result


# добавить новую ссылку на пост для пользователя
def add_to_posts(id_user, link):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO posts (id_user, link, status) VALUES (%s, %s, %s)'
        cursor.execute(sql, (id_user, link, 1))
        conn.commit()
    finally:
        conn.close()


# получить все ссылки пользователя
def get_from_posts(id_user):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'SELECT link FROM posts WHERE id_user = %s AND status = 1'
        cursor.execute(sql, (id_user,))
        result = []
        for row in cursor:
            result.append(row)
    finally:
        conn.close()
    return result


def get_sub_categories():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'SELECT c.name as cat, s.name as subcat FROM categories c, subcategories s ' + \
              'WHERE s.id_category = c.id'
        cursor.execute(sql)
        result = []
        for row in cursor:
            result.append((row['cat'], row['subcat'].split('~')[:-1]))
    finally:
        conn.close()
    return result


def add_to_groups(id_user, group_name):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        sql = 'INSERT INTO groups (id_user, group_name) VALUES (%s, %s)'
        cursor.execute(sql, (id_user, group_name))
        conn.commit()
    finally:
        conn.close()


def make_keyboard():
    # s = '{"buttons": [[{"action": {"type": "location", "payload": "{\"button\": \"1\"}"}}],' + \
    #     '[{"action": {"type": "text", "payload": "{\"button\": \"0\"}", "label": "ЗАКОНЧИТЬ"},"color": "positive"}]'
    s = '{"buttons": [[{"action": {"type": "location", "payload": {\"button\": \"location\"}}}],' + \
        '[{"action": {"type": "text", "payload": {\"button\": \"close\"}, "label": "ЗАКОНЧИТЬ"},"color": "positive"}]'
    categories = get_categories()
    for c in categories:
        id_cat = c['id']
        name_cat = c['name']
        # s += ',[{"action": {"type": "text", "payload": "{\"button\": \"' + str(id_cat + 1) + '\"}",' + \
        #      '"label": "' + name_cat + '"}, "color": "primary"}]'
        s += ',[{"action": {"type": "text", "payload": {\"button\": "category", "id": \"' + str(id_cat + 1) + '\"},' + \
             '"label": "' + name_cat + '"}, "color": "primary"}]'
    s += '], "one_time": false}'
    # print(s)
    return json.loads(s)



# add_to_db(3285241, 2, "Чертаново")
x = get_from_users()  # 19471248  3285241
print(x)
print(get_categories())
# add_to_posts(19471248, 'some_link_1')
# add_to_posts(19471248, 'some_link_2')
# add_to_posts(19471248, 'some_link_3')
print(get_from_posts(19471248))
print(get_sub_categories())
print(make_keyboard())