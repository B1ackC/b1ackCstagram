from sqlalchemy import create_engine

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

    def get_engine(self):
        return self.engine
