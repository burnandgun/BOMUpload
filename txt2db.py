#!/usr/bin/env python
# coding:utf-8
#
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BOMUpload.settings")
#
#
# import django
# if django.VERSION >= (1, 7):
#     django.setup()
#
#
# def main():
#     from BOMContent.models import Part_Con, Part
#
#     p1 = Part.objects.get(ItemNO="A0042-GS-D01-02-07")
#     p2 = Part.objects.get(ItemNO="KLB-C600-DE-11")
#     print p1.Name
#     Part_Con.objects.create(LNO=1,
#                             Head=p1,
#                             Leef=p2,
#                             LeefNum=1,
#                             )
#
#
# if __name__ == "__main__":
#     main()
#     print('中文出来！')