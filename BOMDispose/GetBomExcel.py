import xlrd

data = xlrd.open_workbook('E:\Python project\BOMImport\TxtFile\\bominfo.xls')
table = data.sheet_by_index(0)
xlsContent = []
for i in range(table.nrows):
    tempList = []
    for j in range(table.ncols):
        tempList.append(table.cell(i, j).value)
    xlsContent.append(tempList)
print xlsContent
