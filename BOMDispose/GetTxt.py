# coding =gbk

getTxt = open('E:\Python project\BOMImport\TxtFile\\bominfo.txt')
lineContent = []
txtContent = []
while True:
    getContent = getTxt.readline().decode('GBK')
    if not getContent:
        break
    print getContent
    lineContent.append(getContent)
    txtContent.append(lineContent[len(lineContent)-1].split('\t'))
getTxt.close()
for i in range(len(txtContent)):
    for j in range(len(txtContent[i])):
        print txtContent[i][j]
