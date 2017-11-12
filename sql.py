import pymysql

db = pymysql.connect(
    user='root',
    passwd='password',
    host='192.168.1.71',
    db='conf',
    cursorclass=pymysql.cursors.DictCursor
    # max_connections=8,
    # stale_timeout=300,
)


# db.connect()

def get(query):
    with db.cursor() as cursor:
        cursor.execute(query)
        db.commit()
        return cursor.fetchall()
