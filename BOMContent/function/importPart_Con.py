# -*- coding: utf-8 -*-

# 处理bominfo形成树结构Part_Con

import django
import os

from BOMContent.models import Part, Part_Con
from BOMContent.function.function import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BOMUpload.settings")

if django.VERSION >= (1, 7):
    django.setup()


def dealprocess(list, title):
    RelaNO = titlejudge("RelaNO", title)
    ItemNO = titlejudge("ItemNO", title)
    SequenceNums = titlejudge("SequenceNums", title)
    Num = titlejudge("Num", title)
    for i in range(0, len(list)):
        if int(list[i][RelaNO]) == 1 and ItemNO is not False:
            p = Part.objects.get(ItemNO=list[i][ItemNO])
            del list[i]
            break
    if not Part_Con.objects.filter(LNO=1,
                                   Leef=p,
                                   LeefNum=1,
                                   ).exists():
        Part_Con.objects.create(LNO=1,
                                Leef=p,
                                LeefNum=1,
                                )
    for i in xrange(0, len(list)):
        temp1 = str(list[i][0]).split('.')
        for j in xrange(0, len(list) - 1):
            temp2 = str(list[j][0]).split('.')
            # 从数组中寻找BOM(i)temp1的父部件BOM(j)temp2
            if compareTemp(temp1, temp2) \
                    and ItemNO is not False \
                    and SequenceNums is not False\
                    and Num is not False:
                p1 = Part.objects.get(ItemNO=list[i][ItemNO])
                p2 = Part.objects.get(ItemNO=list[j][ItemNO])
                if not Part_Con.objects.filter(Head=p2,
                                               Leef=p1,
                                               LeefNum=int(list[i][Num]),
                                               ).exists():
                    Part_Con.objects.create(LNO=int(list[i][SequenceNums]),
                                            Head=p2,
                                            Leef=p1,
                                            LeefNum=int(list[i][Num]),
                                            )
                break


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
