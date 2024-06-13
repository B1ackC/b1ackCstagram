import pymysql

class config:
    def __init__(self):
        self.db = pymysql.connect(
            user='root',
            password='root',
            host='localhost',
            port=3306,
            db='blackc',
            charset='utf8'
        )
    # def cursor(self):
    #     return self.db.cursor()

test = config().db.cursor()
print(test)
#
sql = "SELECT * FROM TB_USERS"
test.execute(sql)
print(test.execute(sql))
#
rows = test.fetchall()
print (rows)
test.close()
