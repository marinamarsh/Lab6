import pymysql as MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='toshka',
    passwd='123',
    db='ovoshi',
    charset = 'utf8',
    use_unicode = True
);

c = db.cursor()
c.execute("INSERT INTO tovar (name, `desc`, cout) values ('Помидор Россия', 'Овощи', 44.00)")
db.commit()

c.execute("SELECT * FROM tovar")

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()