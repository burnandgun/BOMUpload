# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xlrd

from django.shortcuts import render
from django.http import HttpResponse


# def home(self, request, *qrgs, **kwargs):
#     form = UploadExcelForm(request.POST, requestFILES)
from pip.utils import logging

from BOMContent.forms import UploadExcelForm
from BOMContent.function.importPart_Con import dealprocess
from BOMContent.models import Part

def home(request):
    return render(request, 'home.html')


def fileupload(request):
    form = UploadExcelForm(request.POST, request.FILES)
    if form.is_valid():
        wb = xlrd.open_workbook(
            filename=None, file_contents=request.FILES['excel'].read())
    table = wb.sheet_by_index(0)
    row = table.nrows
    bom = []
    medium = []
    # 处理从excel中读取的数据
    for i in xrange(1, row):
        col = table.row_values(i)
        # col数组赋值于bom数组，两者相关数据指向同一地址，因此col后改变也可以改变bom数组。可用copy来消除这种情况。
        bom.append(col)
        # 如果为mtlinfo文件，则将所有零部件录入Part数据库。
        if len(col) == 20:
            Part.objects.create(ItemNO=col[1],
                                Name=col[2],
                                EName=col[3],
                                Matrial=col[4],
                                Mass=col[5],
                                Unit=col[6],
                                StandardNumber=col[7],
                                BelongedProNum=col[10],
                                Remark=col[12],
                                DesignType=col[13],
                                ManufactureRemark=col[18],
                                Num=int(col[19]),
                                )
        if len(col) == 22:
            # 弥补修改excel层次号中的1.10为1.1，或者1.20为1.2以此类推的情况。
            if isinstance(col[0], float):
                for j in xrange(0, len(medium)):
                    if col[0] == medium[j]:
                        # 保留2个小数点
                        col[0] = '{:.2f}'.format(col[0])
                if col[0] == 1.0:
                    col[0] = int(col[0])
                medium.append(col[0])
    if len(bom[0]) == 22:
        dealprocess(bom)
    #p = Part.objects.get(ItemNO="A0042-GS-C01-01-00")
    # print(u'%s' % (p.ItemNO.__str__() + "#" + p.Name.__str__()))
    return HttpResponse('ok')
    #  a=1
    #  return HttpResponse('OK')




