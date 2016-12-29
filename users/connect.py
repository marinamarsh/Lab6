import MySQLdb

class Connection:
    def __init__(self, user, passwd, db, host='localhost'):
         self.user = user
         self.passwd = passwd
         self.db = db
         self.host = host
         self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host = self.host,
                user = self.user,
                passwd = self.passwd,
                db = self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()

class Tovar:
    def __init__(self, db_connection, name, desc, cout):
         self.db_connection = db_connection.connection
         self.name = name
         self.desc = desc
         self.cout = cout

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO tovar (`name`, `desc`, cout) values (%s, %s, %s)",
                  (self.name, self.desc, self.cout))
        self.db_connection.commit()
        c.close()

con = Connection('toshka', '123', 'ovoshi')

with con:
    tov = Tovar(con, 'New order', 'Description', 255.25)
    tov.save()