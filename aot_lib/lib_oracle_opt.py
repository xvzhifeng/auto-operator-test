import cx_Oracle
import json
import os
from aot_lib.lib_log import logger

conf_path = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)), "./conf/oracle.json")


class Oracle_opt(object):
    def __init__(self):
        self.conf = self.read_conf()
        self.username = self.conf['username']
        self.password = self.conf['password']
        self.host = self.conf['host']
        self.port = self.conf['port']
        self.database = self.conf['database']
        self.db = self.connect()

    def read_conf(self):
        conf_value = json.loads(conf_path)
        logger.debug(json.dumps(conf_value, default=lambda o: o.__dict__, sort_keys=True, ensure_ascii=False, indent=4))
        return conf_value

    def connect(self):
        tns = cx_Oracle.makedsn(self.host, self.port, self.database)  # 监听Oracle数据库
        db = cx_Oracle.connect(self.username, self.password, tns)  # 连接数据库
        return db

    def select(self, cmd):
        logger.debug("oracle select : " + cmd)
        cursor = self.db.cursor()
        cursor.execute(cmd)
        values = cursor.fetchall()
        logger.debug(values)
        cursor.close()
        return values

    def insert(self, cmd):
        logger.debug("oracle insert : " + cmd)
        cursor = self.db.cursor()
        cursor.execute(cmd)
        cursor.close()
        self.db.commit()

    @property
    def db_opt(self):
        return self.db
