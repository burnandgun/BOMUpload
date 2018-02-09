# -*- coding: utf-8 -*-

from BOMContent.models import *

#将系统中对数据库返回的中文默认格式改为utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#根据从页面获取的数据来选择查询数据库条件，并返回数据库。
def searchdb(name, symbol, value):
    p = Part.objects.filter()
    if name == "ItemNO" and symbol == "equalsym":
        return p.filter(ItemNO=value)
    elif name == "ItemNO" and symbol == "containsym":
        return p.filter(ItemNO__contains=value)
    elif name == "ItemNO" and symbol == "uncontainsym":
        return p.exclude(ItemNO__contains=value)
    elif name == "ItemNO" and symbol == "lequalsym":
        return p.filter(ItemNO__regex='^'+value)
    elif name == "ItemNO" and symbol == "lequalsym":
        return p.filter(ItemNO__regex=value+"$")

    elif name == "Name" and symbol == "equalsym":
        return p.filter(Name=value)
    elif name == "Name" and symbol == "containsym":
        return p.filter(Name__contains=value)
    elif name == "Name" and symbol == "uncontainsym":
        return p.exclude(Name__contains=value)
    elif name == "Name" and symbol == "lequalsym":
        return p.filter(Name__regex="^"+value)
    elif name == "Name" and symbol == "lequalsym":
        return p.filter(Name__regex=value+"$")

    elif name == "Matrial" and symbol == "equalsym":
        return p.filter(Matrial=value)
    elif name == "Matrial" and symbol == "containsym":
        return p.filter(Matrial__contains=value)
    elif name == "Matrial" and symbol == "uncontainsym":
        return p.exclude(Matrial__contains=value)
    elif name == "Matrial" and symbol == "lequalsym":
        return p.filter(Matrial__regex="^"+value)
    elif name == "Matrial" and symbol == "lequalsym":
        return p.filter(Matrial__regex=value+"$")

    elif name == "Mass" and symbol == "equalsym":
        return p.filter(Mass=value)
    elif name == "Mass" and symbol == "containsym":
        return p.filter(Mass__contains=value)
    elif name == "Mass" and symbol == "uncontainsym":
        return p.exclude(Mass__contains=value)
    elif name == "Mass" and symbol == "lequalsym":
        return p.filter(Mass__regex="^"+value)
    elif name == "Mass" and symbol == "lequalsym":
        return p.filter(Mass__regex=value+"$")

    elif name == "StandardNumber" and symbol == "equalsym":
        return p.filter(StandardNumber=value)
    elif name == "StandardNumber" and symbol == "containsym":
        return p.filter(StandardNumber__contains=value)
    elif name == "StandardNumber" and symbol == "uncontainsym":
        return p.exclude(StandardNumber__contains=value)
    elif name == "StandardNumber" and symbol == "lequalsym":
        return p.filter(StandardNumber__regex="^"+value)
    elif name == "StandardNumber" and symbol == "lequalsym":
        return p.filter(StandardNumber__regex=value+"$")

    elif name == "BelongedProNum" and symbol == "equalsym":
        return p.filter(BelongedProNum=value)
    elif name == "BelongedProNum" and symbol == "containsym":
        return p.filter(BelongedProNum__contains=value)
    elif name == "BelongedProNum" and symbol == "uncontainsym":
        return p.exclude(BelongedProNum__contains=value)
    elif name == "BelongedProNum" and symbol == "lequalsym":
        return p.filter(BelongedProNum__regex="^"+value)
    elif name == "BelongedProNum" and symbol == "lequalsym":
        return p.filter(BelongedProNum__regex=value+"$")

    elif name == "Remark" and symbol == "equalsym":
        return p.filter(Remark=value)
    elif name == "Remark" and symbol == "containsym":
        return p.filter(Remark__contains=value)
    elif name == "Remark" and symbol == "uncontainsym":
        return p.exclude(Remark__contains=value)
    elif name == "Remark" and symbol == "lequalsym":
        return p.filter(Remark__regex="^"+value)
    elif name == "Remark" and symbol == "lequalsym":
        return p.filter(Remark__regex=value+"$")

    elif name == "Num" and symbol == "equalsym":
        return p.filter(Num=value)
    elif name == "Num" and symbol == "containsym":
        return p.filter(Num__contains=value)
    elif name == "Num" and symbol == "uncontainsym":
        return p.exclude(Num__contains=value)
    elif name == "Num" and symbol == "lequalsym":
        return p.filter(Num__regex="^"+value)
    elif name == "Num" and symbol == "lequalsym":
        return p.filter(Num__regex=value+"$")


