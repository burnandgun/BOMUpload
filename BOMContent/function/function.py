# -*- coding: utf-8 -*-



#将系统中对数据库返回的中文默认格式改为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#判断字符串string是否在数组listcontent中
def titlejudge(string, listcontent):
    if string in listcontent:
        return listcontent.index(string)
    else:
        return False
