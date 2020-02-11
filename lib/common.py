import psycopg2
import configparser

class db(object):
    # dbコネクション取得メソッド
    def get_connection():
        
        config = configparser.ConfigParser()
        config.read('./conf/common.ini')
        section = "DB"

        connection = psycopg2.connect("host=" + config.get(section, 'host') + 
            " port=" + config.get(section, 'port') + 
            " dbname=" + config.get(section, 'dbname') + 
            " user=" + config.get(section, 'user') + 
            " password=" + config.get(section, 'password'))
        return connection

class test(object):
    # テストメソッド
    def run_test(self):
        print("test def")

