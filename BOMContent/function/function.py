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


# 比较list2层次号是否为list1层次号的前缀，如果是，list2为list1的父部件
def compareTemp(list1, list2):
    if len(list2) == len(list1) - 1:
        for k in xrange(0, len(list2)):
            if list1[len(list1) - 2 - k] == list2[len(list2) - 1 - k]:
                continue
            else:
                return False
        return True
    return False


#将BOM结构在导入数据库之前，整理为JSON格式
def jsonHandle(temp2, jsonContent, RelaNO, p1json,NO ,Num):
    jsontemp = jsonContent
    for i in range(0, len(temp2)):
        for j in range(0, len(jsontemp)):
            if jsontemp[j]["NO"] == int(temp2[i]):
                jsontemp = jsonFormat(jsontemp, j, "Children")
        if i == len(temp2) - 1:
            jsontemp.append({"RelaNO": RelaNO,
                             "ItemNO": p1json[0],
                             "Name": p1json[1],
                             "NO": NO,
                             "Num": Num,
                             "Children": []
                             })


#JSON基本格式
def jsonFormat(jsonContent, j, Children):
    return jsonContent[j][Children]
