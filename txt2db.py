# # !/usr/bin/env python
# # coding:utf-8

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BOMUpload.settings")

import sys
reload(sys)
sys.setdefaultencoding('utf8')


import django
if django.VERSION >= (1, 7):
    django.setup()

from BOMContent.models import *
#
# json = [{'a': 1 ,
#          'b': 2 ,
#          'c': 3,
#          'Children': [{'a': 1 ,
#          'b': 2 ,
#          'c': 3,
#          'Children': [{'a': 1 ,
#          'b': 2 ,
#          'c': 3,
#          'Children': []}]}]}]
#
# a = json[0]['Children']
# b = a[0]['Children']
# c = b[0]['Children']
# c.append({'a' : 1})
#
# print json
# p1 = Part.objects.get(ItemNO="A0042-GS-00")
#
# print str(p1).split('#')[1]
# print Part.objects.all().delete()
# print Part_Con.objects.all().delete()

# a = Part.objects.get(ItemNO__contains="A0038-FPG-00")
# b = a.HeadBJ.all()
# print b


#
# def main():
#     from BOMContent.models import Part_Con, Part
#     Part.objects.create(ItemNO=1, EName=None)
    # a = Part_Con.objects.filter(
    #     Head=p1,
    #     Leef=p2,
    #     LeefNum=1,
    # )
    # print a.exists()

    # try:
    #     a = Part_Con.objects.filter(
    #                             Head=p1,
    #                             Leef=p2,
    #                             LeefNum=1,
    #                             )
    # except:
    #     print "a is not existed"
    # Part_Con.objects.create(LNO=1,
    #                         Head=p1,
    #                         Leef=p2,
    #                         LeefNum=1,
    #                         )
#

# if __name__ == "__main__":
# main()
# #     print('中文出来！')
# a = {"a": 1,
#      "b": 2 }
# print a['a']