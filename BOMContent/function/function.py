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

#使用递归将重复的层次号增加一个小数点补0。
def count(RelaNO, medium):
    for j in xrange(0, len(medium)):
        if str(RelaNO) == str(medium[j]):
            length = len(str(RelaNO).split('.')[len(str(RelaNO).split('.')) - 1])
            # 保留比之前层次号多一位的小数点
            RelaNO = (('%.' + str(length + 1) + 'f') % float(RelaNO))
            #col[RelaNO] = ('{:.' + str(length + 1) + 'f}').format(col[RelaNO])
            RelaNO = count(RelaNO, medium)
            break
    return RelaNO