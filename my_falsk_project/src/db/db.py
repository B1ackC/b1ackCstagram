from .config import dbConfig
from flask import flash

class DBuser:
    def __init__(self):
        self.connect = dbConfig()

    def add_user_from_dto(self, userDto):
        sql = f"INSERT INTO TB_USERS VALUES('{userDto.userId}', '{userDto.userPassword}', '{userDto.userName}')"
        try:
            self.connect.cursor.execute(sql)
            self.connect.db.commit()
            return True
        except Exception as e:
            flash(e)
            return False
        finally:
            self.connect.close()

    # def create_post_from_dto(self, postDto):
    #     insertPost = user(userId=postDto.userId, userPassword=postDto.userPassword, userName=postDto.userName)
    #     self.session.add(insertPost)
    #     self.session.commit()
    #     self.session.close()


