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

# p1 = Part.objects.filter(ItemNO__contains="A0042")

# print Part.objects.all().delete()
# print Part_Con.objects.all().delete()

# a = Part.objects.get(ItemNO__contains="A0038-FPG-00")
# b = a.HeadBJ.all()
# print b


#
# def main():
#     from BOMContent.models import Part_Con, Part
#
#     p1 = Part.objects.get(ItemNO="A0042-GS-D01-02-07")
#     p2 = Part.objects.get(ItemNO="KLB-C600-DE-11")
    # Part_Con.objects.create(LNO=1,
    #                         Head=p1,
    #                         Leef=p2,
    #                         LeefNum=1,
    #                         )
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
#
# if __name__ == "__main__":
# main()
#     print('中文出来！')