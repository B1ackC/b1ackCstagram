import pymysql

class dbConfig:
    def __init__(self):
        self.db = pymysql.connect(
            user='root',
            password='root',
            host='localhost',
            port=3306,
            db='blackc',
            charset='utf8'
        )
        self.cursor = self.db.cursor()

    def fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()

# db = dbConfig()
# sql = "SELECT * FROM TB_USERS"
#
# print(db.fetchall(sql))
# db.close()