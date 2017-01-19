#!/usr/bin/env python
#coding:utf-8

from rediscluster import StrictRedisCluster
from config import Config
import sys
import MySQLdb


class Getuserid(object):
    def redis_cluster(self, keys):
        if not keys:
            return
        redis_nodes = Config.redis_nodes
        try:
            redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
        except Exception, e:
            print "Connect Error!"
            sys.exit(1)
        set_tmp = set()
        for key in keys:

            value = redisconn.get("AtCell_" + key[0])
            if value is not "" and value is not None:
                list = value.split(",")
                set_tmp = set_tmp | set(list)
        str = ",".join(set_tmp)
        return str

    def connectdb(self, uuid):
        if not uuid:
            return
        db = MySQLdb.connect(
            Config.mysql_ip,
            Config.mysql_username,
            Config.mysql_password,
            Config.mysql_dbname,
            charset='utf8')
        try:
            cursor = db.cursor()
            sql = 'select cell_mix from region_cells where uuid = %s;' % uuid
            cursor.execute(sql)
            keys = cursor.fetchall()
            db.close()
            if keys:
                return keys
            else:
                return
        except Exception, e:
            print e
            return

    def getlist(self, uuid):
        uuid = "\'" + uuid + "\'"
        return self.redis_cluster(self.connectdb(uuid))
