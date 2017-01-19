# Create your models here.
# -*- coding:utf-8 -*-

import phoenixdb, json
from config import Config


class SelectDB(object):
    def get_select(self, sql):

        database_url = Config.phoenix_server_url
        try:
            conn = phoenixdb.connect(database_url, autocommit=True)
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception,e:
            print e
            return

    def test_select(self, sql):

        return sql