from .table import user
from .config import DBconfig
from flask import flash

class DBuser:
    def __init__(self):
        self.session = DBconfig().Session()

    # get Connection static
    @staticmethod
    def get_connection():
        if(DBconfig().Session() is None):
            DBconfig().Session()

        return DBconfig().Session()

    def add_user_from_dto(self, userDto):
        searchUser = self.session.query(user).filter_by(userId=userDto.userId).first()
        if searchUser is not None:
            flash("이미 존재하는 아이디입니다.")
            return False
        insertUser = user(userId=userDto.userId, userPassword=userDto.userPassword, userName=userDto.userName)
        self.session.add(insertUser)
        self.session.commit()
        self.session.close()
        return True

    def create_post_from_dto(self, postDto):
        insertPost = user(userId=postDto.userId, userPassword=postDto.userPassword, userName=postDto.userName)
        self.session.add(insertPost)
        self.session.commit()
        self.session.close()


