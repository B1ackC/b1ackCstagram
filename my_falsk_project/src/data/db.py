from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.data.table import user
from flask import flash, redirect

class DBconfig:
    def __init__(self):
        self.db = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': 3306,
            'database': 'blackc'
        }
        self.db_url = f"mysql+pymysql://{self.db['user']}:{self.db['password']}@{self.db['host']}:{self.db['port']}/{self.db['database']}"
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)

class DBcreate:
    def __init__(self):
        self.session = DBconfig().Session()
    def add_user(self, userId, userPassword, userName):
        searchUser = self.session.query(user).filter_by(userId=userId).first()
        if searchUser is not None:
            flash("이미 존재하는 아이디입니다.")
            return False
        insertUser = user(userId=userId, userPassword=userPassword, userName=userName)
        self.session.add(insertUser)
        self.session.commit()
        self.session.close()
        return True

