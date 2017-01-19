#!/usr/bin/env python
#coding:utf-8

import urllib2
import urllib

class Postclient(object):

    def post_to_client(self,url,id_data):

        headers = {"Content-Type": "application/x-www-form-urlencoded"} 
        request = urllib2.Request(url,id_data,headers)
        response=urllib2.urlopen(request)
        content = response.read()
        #这里返回值会被加上“”所以去掉前后双引号
        return  content[1:-1]
    def get_all_list(self,urls,id_data):
        userlist={}
        userlist['CU'] = self.post_to_client(urls[0],id_data)
        userlist['CM'] = self.post_to_client(urls[1],id_data)
        userlist['CT'] = self.post_to_client(urls[2],id_data)
        return userlist
        
        