# -*- coding: utf-8 -*-

# 处理bominfo形成树结构Part_Con

import django
import os

from BOMContent.models import Part, Part_Con

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BOMUpload.settings")

if django.VERSION >= (1, 7):
    django.setup()


def dealprocess(list):
    for i in xrange(1, len(list)):
        temp1 = str(list[i][0]).split('.')
        for j in xrange(0, len(list) - 1):
            temp2 = str(list[j][0]).split('.')
            # 从数组中寻找BOM(i)temp1的父部件BOM(j)temp2
            if compareTemp(temp1, temp2):
                p1 = Part.objects.get(ItemNO=list[i][1])
                p2 = Part.objects.get(ItemNO=list[j][1])
                Part_Con.objects.create(LNO=int(list[i][21]),
                                        Head=p2,
                                        Leef=p1,
                                        LeefNum=int(list[i][19]),
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