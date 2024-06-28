from .config import dbConfig

class DBuser:
    def __init__(self):
        self.connect = dbConfig()

    def add_user_from_dto(self, userDto):
        print (userDto)
        print (userDto.userId, userDto.userPassword, userDto.userName)
        sql = f"INSERT INTO TB_USERS (userId, userPassword, userName)  VALUES('{userDto.userId}', '{userDto.userPassword}', '{userDto.userName}')"
        print(sql)
        try:
            self.connect.fetchall(sql)
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


