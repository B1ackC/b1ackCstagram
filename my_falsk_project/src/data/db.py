from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.data.table import user

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
    def get_session(self):
        return self.Session()

class DBcreate:
    def __init__(self):
        self.session = DBconfig().get_session()
    def add_user(self, userId, userPassword, userName):
        new_user = user(userId=userId, userPassword=userPassword, userName=userName)
        self.session.add(new_user)
        self.session.commit()
        self.session.close()