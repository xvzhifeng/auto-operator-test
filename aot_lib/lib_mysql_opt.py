import mysql.connector
import json
import os
from aot_lib.lib_log import logger

conf_path = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)), "./conf/mysql.json")


class Mysql_opt(object):
    def __init__(self):
        self.conf = self.read_conf()
        self.username = self.conf['username']
        self.password = self.conf['password']
        self.host = self.conf['host']
        self.port = self.conf['port']
        self.database = self.conf['database']
        self.db = self.connect()

    def read_conf(self):
        logger.debug(conf_path)
        conf_value = json.load(open(conf_path, "rb"))
        logger.debug(json.dumps(conf_value, default=lambda o: o.__dict__, sort_keys=True, ensure_ascii=False, indent=4))
        return conf_value

    def connect(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.username,
            passwd=self.password,
            database=self.database
        )  # 连接数据库
        return db

    def select(self, cmd):
        logger.debug("mysql select : " + cmd)
        cursor = self.db.cursor()
        cursor.execute(cmd)
        values = cursor.fetchall()
        logger.debug(values)
        cursor.close()
        return values

    def insert(self, cmd):
        logger.debug("mysql insert : " + cmd)
        cursor = self.db.cursor()
        cursor.execute(cmd)
        cursor.close()
        self.db.commit()

    @property
    def db_opt(self):
        return self.db

if __name__=="__main__":
    mo = Mysql_opt()
    v = mo.select("select * from commands")
    logger.debug(type(v))