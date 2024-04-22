import psycopg2
from backports import configparser

class PostgresConnector:
    def __init__(self, dbname_file='database.txt'):
        self.dbname_file= dbname_file
        self.conn = None
        self.cur = None

    def read_db_credentials(self, dbname):
        try:
            config = configparser.ConfigParser()
            config.read(self.dbname_file)
            if dbname in config:
                return dict(config[dbname])
            else:
                return None 
        except Exception as e:
            print(e)
            return None

    def connect(self, dbname='dds_prod'):
        try:
            creds = self.read_db_credentials(dbname)
            self.conn = psycopg2.connect(**creds)
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)
            return None

    def disconnect(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print(e)
            return None
    
    def execute(self, query):
        try:
            self.cur.execute(query)
            rows = self.cur.fetchall()
            return rows
        except Exception as e:
            print("Error executing query:", e)
            return None