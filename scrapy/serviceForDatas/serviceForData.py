#返回字符串逗号分隔，不包括",id,creater,create_time,updater,update_time"
from scrapy.sql.sql import connectDB, selectOneSql, closeDB, selectAllSql, insertDB
from scrapy.util.util import defaultWrite

#获取表所有的列名，不包括id,creater,create_time,updater,update_time
def getAllCols(dbName,tableName):
    db = connectDB()

    sql = "SELECT GROUP_CONCAT(COLUMN_NAME SEPARATOR ',') FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '" + dbName + "' AND TABLE_NAME = '" + tableName + "'"
    data, flag = selectOneSql(sql, db)
    partToDel = ",id,creater,create_time,updater,update_time"
    requestCols = data[0].strip().replace(partToDel, "")

    closeDB(db)
    return requestCols

#根据表名和搜索公司名称查出所有想改信息
def selectTableInfo(dbName,tableName,key):
    db = connectDB()

    requestCols=getAllCols(dbName,tableName)
    column_list = requestCols.split(",")

    sql = "select "+requestCols+" from "+tableName+" where Company_name = " + "'"+key+"'"
    print(sql)
    # 拼装sql语句
    data, flag=selectAllSql(sql,db)

    #转换为json
    # column_list = []  # 定义字段名的列表
    # for i in fields:
    #     column_list.append(i[0])  # 提取字段名，追加到列表中
    # print column_list　　　　　 # 举例：列表显示结果：['id', 'NAME', 'LOCAL', 'mobile', 'CreateTime']

    jsonlist = list()
    for row in data:  # 一次循环，row代表一行，row以元组的形式显示。
        result = {} # 定义Python 字典
        for i in range(len(column_list)):
            result[column_list[i]] = str(row[i]) # 将row中的每个元素，追加到字典中。

        jsondata = result  # Python的dict --转换成----> json的object
        #print(jsondata)
        jsonlist.append(jsondata)
        #print(jsondata)
    closeDB(db)
    #return json.dumps(jsonlist, ensure_ascii=False),flag
    return jsonlist,flag

#填充字段：num,tableChineseName, tableEnglishName
def refillCompanyTableInfo(dbName):
    db = connectDB()

    # 拼装sql语句
    #获取所有公司名称
    sql = "select company_name from companies "

    companyNames,flag = selectAllSql(sql,db)

    #获取所有table 名称
    sql = "SELECT table_name FROM information_schema.tables WHERE table_schema = '"+dbName+"' AND table_type = 'base table' "

    tableNames, flag= selectAllSql(sql, db)
    print(tableNames)
    print(companyNames)
    companyNames=companyNames
    count = 0
    #遍历tableName和companyNames获取和填充对应内容
    for i in companyNames:
        for j in tableNames:
            tableName = j[0]
            companyName = i[0]
            if count == 3:
                print("xx")
            if tableName != 'companies' and tableName != 'dictionary' and tableName != "company_table_info":
                print("times: "+str(count))
                count = count + 1
                sql = "select count(*) from "+tableName+" where "+"'"+companyName+"'="+"Company_name"
                print(sql)
                data,flag=selectAllSql(sql,db)
                num=data[0][0]

                if num > 0:
                    num = str(num)
                    sql= "select chinese from dictionary where "+"'"+tableName+"'="+"english"
                    data,flag=selectOneSql(sql,db)

                    tableChineseName="'"+data[0]+"'"

                    tableEnglish = "'"+tableName+"'"

                    companyName = "'"+companyName+"'"

                    sql = "insert into company_table_info (company_name,table_english_name,table_chinese_name,num_info) values ("+companyName+","+tableEnglish+","+tableChineseName+","+num+")"
                    print(sql)
                    try:
                        affectRows=insertDB(db,sql)
                        print(sql)
                    except Exception as e:
                        defaultWrite( "C:/Users/admin/Desktop/pachong_result/sql/",sql)
                        pass
            else:
                print(tableName+"///////////////////")
    closeDB(db)

#判断是否存在公信名称,如果存在直接返回内容
def checkCompany(key):
    db=connectDB()

    #拼装sql语句
    newkey = "'"+key+"'"
    sql="select company_name from companies where company_name = "+newkey
    data,flag=selectOneSql(sql,db)
    if flag >= 1:
        data, flag = selectTableInfo("scrapy", "company_table_info", key)
    closeDB(db)

    return data,flag


#获取字典内容
def getDictionary(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    affectRows = cursor.execute("select english,chinese from dictionary")
    print(affectRows)
    result = cursor.fetchone()
    dictionary = dict()
    while result != None:
        dictionary[result[1]] = result[0]
        print(result, cursor.rownumber)
        result = cursor.fetchone()

# 增加一行数据，tableType1
def addRow1(row_values):
    pos = 0
    toReturn = ""
    while pos < len(row_values):
        toReturn = toReturn + row_values[pos] + ","
        pos = pos + 1

    # 删除最后一个逗号
    toReturn = toReturn[:-1]
    return toReturn,pos

# 增加一行数据，tableType2
def addRow2(values, tableName, companyCode):
    # 为每一行
    for row_values in values:
        row_values.append(tableName)
        row_values.append(companyCode)

        pos = 0
        toReturn = ""
        while pos < len(row_values):
            for value in row_values[pos]:
                toReturn = toReturn +"'" +row_values[pos] +"'"+ ","
                pos = pos + 1
            # 删除最后一个逗号
            toReturn = toReturn[:-1]
            toReturn = "("+toReturn+"),"

        # 删除最后一个逗号
        toReturn = toReturn[:-1]

        return toReturn,pos

#插入获取信息至数据库
def insertInfo(items, companyCode):
    db = connectDB()

    # 解析字段和内容
    for item in items:
        sql = item[1][0]
        moduleName = item[0]
        print(moduleName)
        print(sql)
        affectedRow = insertDB(db, sql)
        if affectedRow <= 0:
            return -1

    #保存被搜索的公司名称
    sql = "insert  into companies (company_name) values ('"+companyCode+"')"
    affectedRow=insertDB(db,sql)
    if affectedRow <= 0:
        return -1
    db = closeDB(db)