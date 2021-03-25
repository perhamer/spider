import time

import xlwt as xlwt


def export(result):
    wb = xlwt.Workbook()
    # 添加一个表
    ws = wb.add_sheet('test')
    # 定义表头
    ws.write(0, 0, '标题')
    ws.write(0, 1, '链接')
    for rowNum in range(0, len(result)):
        for colNum in range(0, len(result[rowNum])):
            # 需要注意的是行号和列号都是从0开始的
            ws.write(rowNum + 1, colNum, str(result[rowNum][colNum]))
    # 保存excel文件
    wb.save('./file/' + str(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))+'_'+str(len(result)) + '条.xls')

