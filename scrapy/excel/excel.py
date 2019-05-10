from xlutils.copy import copy
import xlrd

# 检查sheet名字，如果没有，就创建，并且返回list<tuple>,tuple:(index,sheetname)
def checkSheetName(sheetsName, excelPath):
    # 初始化返回值
    toReturn = list()

    # 打开读excel
    readbook = xlrd.open_workbook(excelPath)
    sheets = readbook.sheet_names()

    # 打开写excel
    writebook = copy(readbook)  # copy后的readbook就是一个workbook对象

    count = 0
    # 遍历参数名称
    for name in sheetsName:
        # 如果没有，就创建
        if not (sheets.__contains__(name)):
            writebook.add_sheet(name)
            writebook.save(excelPath)
        toReturn.append((count, name))
        count = count + 1

    return toReturn

# 增加一个新字段
def checkColumn(workbook, numSheet, info, excelPath):
    sheet = workbook.sheet_by_index(numSheet)
    ncols = sheet.ncols  # 列

    # 如果不存在字段，做添加行为
    if getCol(info, sheet) == -1:
        newbook = copy(workbook)
        newsheet = newbook.get_sheet(numSheet)
        newsheet.write(0, ncols, info)
        newbook.save(excelPath)

# 根据字段，判断列的位置
def getCol(str, sheet):
    ncols = sheet.ncols  # 列
    i = 0
    while i < ncols:
        name = sheet.cell(0, i).value  # 获取0行i列的表格值
        if name == str:
            return i
        i = i + 1

    return -1

# 根据sheet名称获取pos，可以直接借助checkSheetName的返回值
def getSheetPos(sheetName, workbook):
    sheetNames = workbook.sheet_names()
    count = 0
    for isheetName in sheetNames:
        if isheetName == sheetName:
            return count
        count = count + 1
    return -1



