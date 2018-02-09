# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import xlrd


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# def home(self, request, *qrgs, **kwargs):
#     form = UploadExcelForm(request.POST, requestFILES)
from django.views.decorators.csrf import csrf_exempt
from pip.utils import logging

from BOMContent.function.importPart_Con import *
from BOMContent.function.searchDB import *
from BOMContent.function.function import *
from BOMContent.models import Part


import sys
print sys.getdefaultencoding()
sys.setdefaultencoding('utf-8')


#导入bom以及txt转换视图
def bomupload(request):
    return render(request, 'home.html')


#操作bom表，并将其导入数据库
@csrf_exempt
def fileupload(request):
    wb = xlrd.open_workbook(filename=None, file_contents=request.FILES.get('excel').read())
    if request.FILES.get('excel').name.split('.')[-1] not in ['xls', 'xlsx']:
        return render(request, 'wronghtml.html', {'str': "上传的不是excel文档"})
    table = wb.sheet_by_index(0)
    row = table.nrows
    bom = []
    medium = []
    temppart = len(Part.objects.all())
    temppartCon = len(Part_Con.objects.all())
    # itemNO = None
    # # 将txt中的数据分散读取，来寻找当前文档的物号
    # for i in range(1, row):
    #     col = table.row_values(i)
    #     if col[2] == '蒸汽分配管' or col[2] == '管束总成':
    #         itemNO = (col[1].split('-'))[0]
    try:
        # 识别excel第一行小标题，进行对对应列内容的列号的识别
        title = table.row_values(0)
        ItemNO = titlejudge("ItemNO", title)
        Name = titlejudge("Name", title)
        EName = titlejudge("EName", title)
        Matrial = titlejudge("Matrial", title)
        Mass = titlejudge("Mass", title)
        Unit = titlejudge("Unit", title)
        StandardNumber = titlejudge("StandardNumber", title)
        BelongedProNum = titlejudge("BelongedProNum", title)
        Remark = titlejudge("Remark", title)
        DesignType = titlejudge("DesignType", title)
        ManufactureRemark = titlejudge("ManufactureRemark", title)
        RelaNO = titlejudge("RelaNO", title)
        # 处理从excel中读取的数据
        for i in xrange(1, row):
            col = table.row_values(i)
            #col[1] = itemNO + '-' + col[1]
            # col数组赋值于bom数组，两者相关数据指向同一地址，因此col后改变也可以改变bom数组。可用copy来消除这种情况。
            bom.append(col)
            # 如果文件包含层次号，弥补修改excel层次号中的1.10为1.1，或者1.20为1.2以此类推的情况。便于处理为Part_Con
            if RelaNO is not False:
                if isinstance(col[RelaNO], float):
                    for j in xrange(0, len(medium)):
                        if col[RelaNO] == medium[j]:
                            # 保留2个小数点
                            col[RelaNO] = '{:.2f}'.format(col[RelaNO])
                    if col[RelaNO] == 1.0:
                        col[RelaNO] = int(col[RelaNO])
                    medium.append(col[RelaNO])
            #将所有零部件录入Part数据库。
            try:
                if ItemNO is not False\
                    and Name is not False \
                    and EName is not False \
                    and Matrial is not False \
                    and Mass is not False \
                    and Unit is not False \
                    and StandardNumber is not False \
                    and BelongedProNum is not False \
                    and Remark is not False \
                    and DesignType is not False \
                    and ManufactureRemark is not False:
                    Part.objects.create(ItemNO=col[ItemNO],
                                        Name=col[Name],
                                        EName=col[EName],
                                        Matrial=col[Matrial],
                                        Mass=col[Mass],
                                        Unit=col[Unit],
                                        StandardNumber=col[StandardNumber],
                                        BelongedProNum=col[BelongedProNum],
                                        Remark=col[Remark],
                                        DesignType=col[DesignType],
                                        ManufactureRemark=col[ManufactureRemark],
                                        )
            except:
                if RelaNO is False:
                    return render(request, 'wronghtml.html', {'str': "上传的文件不是整理过的BOM文档或者BOM已上传！"})
                continue
        if RelaNO is not False:
        # 使用dealprocess将bominfo中的数据处理为Part_Con
            dealprocess(bom, title)
        #p = Part.objects.get(ItemNO="A0042-GS-C01-01-00")
        # print(u'%s' % (p.ItemNO.__str__() + "#" + p.Name.__str__()))
        if temppart == len(Part.objects.all()) and temppartCon == len(Part_Con.objects.all()):
            return render(request, 'wronghtml.html', {'str': "未更新数据库！上传文档有误或者BOM已上传!"})
        return render(request, 'bomupload.html')
        #  a=1
        #  return HttpResponse('OK')
    except:
        return render(request, 'wronghtml.html', {'str': "上传的文件不是整理过的文档或者BOM已上传"})

# 上传txt并存入数据库
@csrf_exempt
def textchange(request):
    file = request.FILES.get('file')
    tempjudge = file.name.split('.')
    if not tempjudge[1] == 'txt':
        return render(request, 'wronghtml.html', {'str': "上传的不是txt文档"})
    bom = []
    medium = []
    templine = []
    temppart = len(Part.objects.all())
    temppartCon = len(Part_Con.objects.all())
    for line in file:
        templine.append(line.decode('gbk').replace('\n', ''))
    try:
        # 识别excel第一行小标题，进行对对应列内容的列号的识别
        title = templine[0].split('\t')
        ItemNO = titlejudge("ItemNO", title)
        Name = titlejudge("Name", title)
        EName = titlejudge("EName", title)
        Matrial = titlejudge("Matrial", title)
        Mass = titlejudge("Mass", title)
        Unit = titlejudge("Unit", title)
        StandardNumber = titlejudge("StandardNumber", title)
        BelongedProNum = titlejudge("BelongedProNum", title)
        Remark = titlejudge("Remark", title)
        DesignType = titlejudge("DesignType", title)
        ManufactureRemark = titlejudge("ManufactureRemark", title)
        RelaNO = titlejudge("RelaNO", title)
        for i in range(1, len(templine)):
            col = templine[i].split('\t')
            # col数组赋值于bom数组，两者相关数据指向同一地址，因此col后改变也可以改变bom数组。可用copy来消除这种情况。
            bom.append(col)
            # 如果为mtlinfo文件，则将所有零部件录入Part数据库。
            # 如果文件包含层次号，弥补修改excel层次号中的1.10为1.1，或者1.20为1.2以此类推的情况。便于处理为Part_Con
            if RelaNO is not False:
                # 弥补修改excel层次号中的1.10为1.1，或者1.20为1.2以此类推的情况。便于处理为Part_Con。只适用于总装图中部套数量100以下的情况
                if isinstance(col[RelaNO], float):
                    for j in xrange(0, len(medium)):
                        if col[RelaNO] == medium[j]:
                            # 保留2个小数点
                            col[RelaNO] = '{:.2f}'.format(col[0])
                    if col[RelaNO] == 1.0:
                        col[RelaNO] = int(col[RelaNO])
                    medium.append(col[RelaNO])
                #将零部件信息保存于数据库
            try:
                if ItemNO is not False \
                        and Name is not False \
                        and EName is not False \
                        and Matrial is not False \
                        and Mass is not False \
                        and Unit is not False \
                        and StandardNumber is not False \
                        and BelongedProNum is not False \
                        and Remark is not False \
                        and DesignType is not False \
                        and ManufactureRemark is not False:
                    Part.objects.create(ItemNO=col[ItemNO],
                                        Name=col[Name],
                                        EName=col[EName],
                                        Matrial=col[Matrial],
                                        Mass=col[Mass],
                                        Unit=col[Unit],
                                        StandardNumber=col[StandardNumber],
                                        BelongedProNum=col[BelongedProNum],
                                        Remark=col[Remark],
                                        DesignType=col[DesignType],
                                        ManufactureRemark=col[ManufactureRemark],
                                        )
            except:
                if RelaNO is False:
                    return render(request, 'wronghtml.html', {'str': "上传的文件不是整理过的BOM文档或者BOM已上传！"})
                continue
        if RelaNO is not False:
        # 使用dealprocess将bominfo中的数据处理为Part_Con
            dealprocess(bom, title)
        if temppart == len(Part.objects.all()) and temppartCon == len(Part_Con.objects.all()):
            return render(request, 'wronghtml.html', {'str': "未更新数据库！上传文档有误或者BOM已上传!"})
        return render(request, 'bomupload.html')
    except:
        # return render(request, 'wronghtml.html', {'str': "上传的文件不是整理过的文档或者BOM已上传"})
        return render(request, 'wronghtml.html', {'str': "上传的文件不是整理过的BOM文档或者BOM已上传!"})


#查询数据库视图
def index(request):
    return render(request, 'report.html')


#查询数据库操作
@csrf_exempt
def PDM_PartSearch(request):
    #从模板中用json获取数据
    query_info = json.loads(request.GET['query_info_json'])
    data = searchdb(query_info['name'], query_info['symbol'], query_info['value'])
    if data:
        return HttpResponse(data)
    else:
        return HttpResponse('输入的项目号或者搜索条件有误')



#查询数据库视图
def BOMSearch(request):
    return render(request, 'html.html')
