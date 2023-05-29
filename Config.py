import os

from dotenv import load_dotenv

load_dotenv()

class Config:

    mysql_host = os.getenv('MYSQLDB_HOST')
    mysql_port = int(os.getenv('MYSQLDB_PORT'))
    mysql_user = os.getenv('MYSQLDB_USER')
    mysql_pwd = os.getenv('MYSQLDB_PWD')
    mysql_db = os.getenv('MYSQLDB_DB')
