# coding=utf-8

import urllib2

#admin_user_login 商家后台
#admin_login 管理后台

def getCapture(type='sj',ssid=None):
    url = 'http://tete.haodou.com/interface/code.php?option=%s'%((type=='sj'and'admin_user_login')or(type=='gl'and'admin_login') or '')
    headers = {'Cookie':'YCSSID=%s'%ssid}
    req = urllib2.Request(url,headers = headers)
    return urllib2.urlopen(req).read()