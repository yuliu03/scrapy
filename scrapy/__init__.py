import json
import re
import sys
import time
import uuid

from bs4 import BeautifulSoup
from django.http import HttpResponse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 初始化公司名称，用于记录异常
from scrapy.detailStructureScrapy.detailStructureScrapy import *
from scrapy.myException.myException import *
from scrapy.serviceForDatas.serviceForData import *
from scrapy.sql.sql import *
from scrapy.util.util import *
from scrapy.loginUtil.login import *


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

#更换验证码
def changVerifiedCode(infoDic):
    #sessionInfo[myid]["wait"],myid
    img=infoDic["imgObj"]
    browser=infoDic["browser"]
    wait=infoDic["wait"]
    # 验证码更新
    ActionChains(browser).click(img).perform()
    time.sleep(0.5)
    # 获取验证图片，base64编码，可以通过html展示
    img = browser.find_element_by_xpath("//div[@id='nc_1__imgCaptcha_img']/img")
    verifiedCode = img.get_attribute("src")
    res = {'msg': '验证码', 'msg_code': 1001, 'data': verifiedCode}  # 1001表示成功,返回验证码

    infoDic["browser"] = browser
    infoDic["wait"] = wait
    infoDic["imgObj"] = img


    return HttpResponse(json.dumps(res, ensure_ascii=False)),infoDic

#判断验证码信息，如果正确，点击进入搜索页面
def checkVerifiedCode(code,browser,wait,myid,sessionTime=0.4):
        try:
            # 填写验证码信息
            inputCode = browser.find_element_by_id("nc_1_captcha_input")
            inputCode.send_keys(code)
            print("验证码获取成功")

            # 提交验证
            submitButton = browser.find_element_by_xpath("//div[@id='nc_1_scale_submit']/span")
            webdriver.ActionChains(browser).double_click(submitButton).perform()
            print("验证码提交成功")

            # 确认是否出现验证码输入错误提示
            try:
                time.sleep(0.5)
                span = browser.find_element_by_xpath("//div[@id='nc_1__captcha_img_text']/span[@class='nc-lang-cnt']")
                text = span.get_attribute('innerHTML')
                print(text)
                return -1
            except:
                print("验证码验证成功")


            # 判断session id 是否生成
            time.sleep(sessionTime)
            sessionId = browser.find_element_by_xpath("//input[@id='csessionid_one']").get_attribute("value")
            if (sessionId == ""):
                print("未生成session id")
                return -2

            # //*[@id="user_login_normal"]/button/strong
            button = browser.find_element_by_xpath("//*[@id='user_login_normal']/button")
            button.click()

            # 回车
            # inputCode.send_keys(Keys.ENTER)

        except sessionIdError as e:
            raise sessionIdError(e.errorinfo)

        except codeError as e:
            raise codeError(e.errorinfo)

        flag = 0

        toReturn = {}
        toReturn["browser"] = browser
        toReturn["wait"] = wait
        toReturn["myid"] = myid
        return flag,toReturn

#请求获取验证码信息
def requestLogin(chromeDir,acount,password,loginDir):
    searchDir = chromeDir

    browser = webdriver.Chrome(searchDir)

    try:
        # 设置浏览器需要打开的url
        browser.get(loginDir)

        # 默认浏览器等待时间100秒
        wait = WebDriverWait(browser, 100)

        # 选择账号密码登录方式
        wait.until(EC.presence_of_element_located((By.ID, "normalLogin")))
        botton = browser.find_element_by_id("normalLogin")
        botton.click()

        # 自动添加
        name = browser.find_element_by_id("nameNormal")
        name.send_keys(acount)#13958127726
        pwd = browser.find_element_by_id("pwdNormal")
        pwd.send_keys(password)#87096927

        # 移动鼠标滑块验证码
        time.sleep(0.2)
        wait.until(EC.presence_of_element_located((By.ID, "nc_1_n1z")))
        move_k = browser.find_element_by_id("nc_1_n1z")
        ActionChains(browser).drag_and_drop_by_offset(move_k, 341, 0).perform()

        try:
            # 等待验证码图片出现
            try:
                wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='nc_1__imgCaptcha_img']/img")))
            except:
                raise netError("网络连接失败")

            # 获取验证图片，base64编码，可以通过html展示
            img = browser.find_element_by_xpath("//div[@id='nc_1__imgCaptcha_img']/img")
            verifiedCode = img.get_attribute("src")
            return verifiedCode,browser,wait,img


        except sessionIdError as e:
            raise sessionIdError(e.errorinfo)

        except codeError as e:
            raise codeError(e.errorinfo)

    except TimeoutException as e:
        raise TimeoutException(e.msg)

# 搜索栏搜索公司信息
def searchOne(companyCode,browser,wait):
    try:
        # 等待搜索框出现
        wait.until(EC.presence_of_element_located((By.ID, "searchkey")))

        # 填写搜索内容
        search = browser.find_element_by_id("searchkey")
        search.send_keys(companyCode)

        # 定位搜索按钮并且点击触发
        doSearch = browser.find_element_by_id("V3_Search_bt")
        doSearch.click()

        return browser,wait

    except netError as e:
        raise netError("网络不稳定，请重新连接")

#匹配搜索结果列表内容和搜索具体字段
def selectForOne(companyCode, browser, wait):
    resultNum='0'

    # 等待结果数量显示
    # pageResource(browser,wait)
    # wait.until(EC.presence_of_element_located((By.ID, "//*[@id='countOld']")))
    # 获取结果数量
    num = browser.find_element_by_xpath("//*[@id='countOld']/span").text
    if num == '0':  # 判断是否有结果
        print("no result: " + "[result number: " + num + "]")
        return resultNum

    resultName = browser.find_element_by_xpath("//*[@id='search-result']/tr[1]/td[3]/a").text
    if resultName != companyCode:  # 判断字段是否绝对一样
        resultNum='-1'
        print("[companyCode: " + companyCode + "]"
              + "result company name: " + resultName)
        return resultNum, browser, wait

    else:
        # 确认找到结果
        resultNum = num

        # 等待列表信息展示结束
        wait.until(EC.presence_of_element_located((By.ID, "search-result")))

        # 打印页面内容
        # pageResource(browser)

        # 获取列表信息
        resultList = browser.find_element_by_xpath("//tbody[@id='search-result']")

        # 获取每条信息明细
        trs = resultList.find_elements_by_xpath(".//tr")

        # 默认第一条
        firstTd = trs[0].find_elements_by_xpath(".//td")
        # print(firstTd)
        # 获取链接
        a = firstTd[2].find_elements_by_xpath("./a")[0].get_attribute("href")

        # 点击进入公司明细页面
        browser.get(a)
        wait.until(EC.presence_of_all_elements_located)
        # pageResource(browser)

        #resultNum 为查询结果数量，因为是模糊查询，所以会出现多个结果
        return resultNum, browser, wait


# 方法一：获取所有菜单链接
def getNav(browser, wait, rootUrl):
    # 提取页面源代码
    content = browser.page_source.encode('utf-8')
    soup = BeautifulSoup(content, 'lxml')

    # 提取目录行内容
    navs = soup.findAll('a', {'class': 'company-nav-head'})

    # 初始化公司内容目录字典： key：标题，value：相对路径
    navsList = list()

    # 获取目录信息
    for item in navs:
        href = item['href']
        title = item.find('h2').text
        numInfo = item.find('span').text
        # print(title,href,numInfo)
        navsList.append((title, rootUrl + href, numInfo))

    return browser, wait, navsList

# 方法二：通过点击目录，直接获取所有内容
def getClassName(name):
    if name == '基本信息':
        return "base_info", "base_div"
    elif name == '法律诉讼':
        return "susong_info", "susong_div"
    elif name == '经营状况':
        return "run_info", "run_div"
    elif name == '经营风险':
        return "fengxian_info", "fengxian_div"
    elif name == '企业发展':
        return "report_info", "report_div"
    elif name == '知识产权':
        return "assets_info", "assets_div"
    elif name == '历史信息':
        return "history_info", "history_div"
    elif name == '上市信息':
        return "ipo_info", "ipo_div"

# 根据每个目录开始爬取内容
def beginNav( browser, wait):

    # 获取所有目录项目
    navs = browser.find_elements_by_xpath("//a[@class='company-nav-head ']")

    # 手动加入VIP项目：历史信息
    try:
        navs.append(browser.find_element_by_xpath("//*[@id='history_title']"))
    except Exception as e:
        pass

    # 初始化公司信息内容储存表
    items = list()

    # 遍历，判断每目录项目中是否有信息
    for nav in navs:
        numInfo = nav.find_element_by_xpath("span").text.strip()
        name = nav.find_element_by_xpath("h2").text.strip()

        # 判断是否有内容
        if numInfo != '0':
            nav.click()  # 点击加载页面内容,每次点击后，后台会添加内容
            className, id = getClassName(name)  # 获取内容对应的id和class名称
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, className)))  # 等待刷新完毕

            # 转为soup
            content = browser.page_source.encode('utf-8')
            soup = BeautifulSoup(content, 'lxml')

            # 根据id定位模块
            div = soup.find('div', {'id': id})

            # 开始爬取数据, type:<tuple>
            moduleInfo = contentPage(div, name)

            # 需要把内容根据名字放入列表中
            if moduleInfo[1] != None:
                items.append(moduleInfo)

    return items

# 根据选择获取模块内容
def contentPage(soup, option):
    # 初始化模块信息储存空间
    moduleInf = None

    if option == "基本信息":
        # 获取基本信息模块信息
        print("基本信息")
        moduleInf = basicInfo(soup)
    elif option == "法律诉讼":
        # 获取法律诉讼信息
        print("法律诉讼")
        moduleInf = legalAction(soup)
    elif option == "经营状况":
        # 获取经营状况信息
        print("经营状况")
        moduleInf = runState(soup)
    elif option == "经营风险":
        # 获取经营风险信息
        print("经营风险")
        moduleInf = runRisk(soup)
    elif option == "企业发展":
        # 获取企业发展信息
        print("企业发展")
        moduleInf = companyDev(soup)
    elif option == "历史信息":
        # 获取企业发展信息
        print("历史信息")
        moduleInf = historyInfo(soup)
    elif option == '上市信息':
        # 获取企业上市信息
        print("上市信息")
        moduleInf = ipoInfo(soup)

    return (option, moduleInf)
    # 目前知识产权一栏不处理
    # elif option=="知识产权":
    #     #获取知识产权信息
    #     print("知识产权")
    #     #IntellectualPro(soup)

def insertInfo(items, companyCode,dic):
    # 解析字段和内容
    tableNames = list()
    tableKeysValues = list()  # list<tableType,keys,values,tableName>
    print("////////////////")
    # 循环所有的模块
    for item in items:
        # 循环所有的table
        for x in item[1]:
            # 初始化
            keys = list()
            values = list()

            # 获取table名称，也是sheet 的名称
            if x[0].__str__() == "行政处罚 [工商局]":
                tableName = "行政处罚"
            else:
                tableName = x[0].__str__()

            tableNames.append(tableName)

            # print("tableName: " +tableName)
            info = x[1]
            tableType = info[0]
            table = info[1]

            # 判断，数字1为上下类型table
            if tableType == 1:
                keys = table[0]
                values = list()

                # 获取所有table对应的内容
                pos = 1
                while pos < len(table):
                    values.append(table[pos])
                    pos = 1 + pos

                # 写死加入公司名称和模块名称，需要保持key和value的位置一致
                keys.append("module_name")
                keys.append("company_name")

                tableKeysValues.append((tableType, keys, values, tableName))

            # 判断，数字1为左右类型table
            elif tableType == 0:
                print("table: " + table.__str__())
                for i in table:
                    keys.append(i[0])
                    values.append(i[1])

                # 写死加入公司名称和模块名称，需要保持key和value的位置一致
                keys.append("module_name")
                keys.append("company_name")

                tableKeysValues.append((tableType, keys, values, tableName))

        print("----------")
        # print("table name: "+item[1][0].__str__())
        # print("----------")
        # print("table type: " + item[1][1][0].__str__())
        # print("----------")
        # print("table info: " + item[1][1][1].__str__())

    print(tableKeysValues)
    print("////////////////")

    # 遍历所有的模块
    for i in tableKeysValues:
        tableType = i[0]
        keys = i[1]
        values = i[2]


        #拼装sqlkeys
        #初始化参数
        sqlkeys = ""
        sqlValues = ""
        countKeys = 0
        countValues = 0

        for key in keys:
            # 打开excel
            sqlkeys = dic[key] + ","
            countKeys = countKeys + 1

        #去除最后一个逗号
        sqlkeys = sqlkeys[:-1]
        sqlkeys ="("+sqlkeys+")"

        # 判断，数字1为上下类型table
        if tableType == 0:
            values.append(tableName)
            values.append(companyCode)
            sqlValues,countValues=addRow1(values)
        # 判断，数字1为左右类型table
        elif tableType == 1:
            sqlValues,countValues=addRow2(values,tableName,companyCode)

        if countValues != countKeys:
            raise sqlError("拼装sql出错")

        else:
            finalSql = "insert into" + dic[tableName]+sqlkeys+" values "+values
            print(finalSql)

def doScrapyForOneKey(key,browser,wait):
        # 第一个公司，名称
        companyCode = key

        ###############################
        # 进入主页面
        ###############################
        # 搜索公司信息
        print("-----开始搜索-----")
        browser, wait=searchOne(companyCode,browser,wait)
        print("-----结束搜索-----")

        ###############################
        # 进入主搜索结果列表页面
        ###############################
        print("-----开始对搜索结果进行操作-----")
        resultNum, browser, wait = selectForOne(companyCode, browser, wait)
        print("-----结束对搜索结果进行操作-----")
        ###############################
        # 获取所有菜单链接
        ###############################

        if resultNum == '0':
            return '0'

        if resultNum == '-1':
            return '-1'


        print("-----开始对公司信息目录进行操作-----")
        items = beginNav( browser, wait)
        print("-----结束对公司信息目录进行操作-----")
        print("===========写入内容至本地文本=================")
        #writeResult(output, items, companyCode)

        #获取sql语句拼装信息
        db = connectDB()

        #获取字典内容
        dictionary=getDictionary(db)

        #插入内容至db
        insertInfo(items,companyCode,dictionary)

        db = closeDB(db)
        #返回内容
        return items
    #return doScrapyForOneKey(key,browser, wait)

########################################################

# browser = ""
# wait = ""
# key = ""
# img = ""
# chromeDir = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 这里是你的驱动的绝对地址
# # firefoxDir="D:/firefox/geckodriver.exe"
# loginDir = "https://www.qichacha.com/user_login"
#
# acount = "13958127726"
# password = "87096927"

#server=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动



#判断公司名称是否存在


#refillCompanyTableInfo("scrapy")

# preBegin()
# time.sleep(2)
# changVerifiedCode()

#@server.route('/preBegin',methods=['post'])#只有在函数前加上@server.route (),这个函数才是个接口，不是一般的函数
def requestInfoHttpResponseJson(key,chromeDir,acount,password,loginDir):
    toReturn = dict()
    if key=="" or key == None:
        res = {'msg': '必填字段未填，请查看接口文档', 'msg_code': 1001}  # 1001表示必填接口未填
    else:
        try:
            print(key)
            data,flag=checkCompany(key)
            if flag >= 1:
                res = {'msg': '信息', 'msg_code': 1000,'data':data}  # 1000表示成功
            else:
                print("-----开始登录-----")
                verifiedCode, browser, wait, imgObj = requestLogin( chromeDir, acount, password,loginDir)
                print("-----结束登录-----")
                myid=uuid.uuid1().hex
                res = {'msg': '验证码', 'msg_code': 1001, 'data': verifiedCode, 'myid':myid}  # 1001表示成功,返回验证码
                toReturn["browser"] = browser
                toReturn["wait"] = wait
                toReturn["imgObj"] = imgObj
                toReturn["myid"]=myid
                toReturn["companyCode"]=key
        except netError as e:
            res = {'msg': '网络不稳定', 'msg_code': 1002}  # 1002表示网络错误
            browser.close()

    return HttpResponse(json.dumps(res,ensure_ascii=False)),toReturn


def requestInfoScrapy(key,chromeDir,acount,password,loginDir):
    toReturn = dict()
    if key=="" or key == None:
        res = {'msg': '必填字段未填，请查看接口文档', 'msg_code': 1003}  # 1003表示必填接口未填
    else:
        try:
            print(key)
            data,flag=checkCompany(key)
            if flag >= 1:
                res = {'msg': '信息', 'msg_code': 1000,'data':data}  # 1000表示成功，返回信息
            else:
                print("-----开始登录-----")
                verifiedCode,browser,wait,imgObj = requestLogin(chromeDir,acount,password,loginDir)
                print("-----结束登录-----")
                res = {'msg': '验证码', 'msg_code': 1001,'data':verifiedCode}  # 1001表示成功,返回验证码
                toReturn["browser"]=browser
                toReturn["wait"]=wait
                toReturn["imgObj"] = imgObj
        except netError as e:
            res = {'msg': '网络不稳定', 'msg_code': 1002}  # 1002表示网络错误
            browser.close()
    print(res)
    return res,toReturn


# 从搜索结果中选择公司，返回相关链接
# def select(wait, browser, companyCode):
#     # resultNum 判断搜索结果数量
#     resultNum = '0'
#
#     # 等待结果数量显示
#     # pageResource(browser,wait)
#     # wait.until(EC.presence_of_element_located((By.ID, "//*[@id='countOld']")))
#     # 获取结果数量
#     num = browser.find_element_by_xpath("//*[@id='countOld']/span").text
#     if num == '0':  # 判断是否有结果
#         print("no result: " + "[result number: " + num + "]")
#
#         return browser, wait, resultNum
#
#     resultName = browser.find_element_by_xpath("//*[@id='search-result']/tr[1]/td[3]/a").text
#     if resultName != companyCode:  # 判断字段是否绝对一样
#         print("[companyCode: " + companyCode + "]"
#               + "result company name: " + resultName)
#         return browser, wait, resultNum
#
#     else:
#         # 确认找到结果
#         resultNum = num
#
#         # 等待列表信息展示结束
#         wait.until(EC.presence_of_element_located((By.ID, "search-result")))
#
#         # 打印页面内容
#         # pageResource(browser)
#
#         # 获取列表信息
#         resultList = browser.find_element_by_xpath("//tbody[@id='search-result']")
#
#         # 获取每条信息明细
#         trs = resultList.find_elements_by_xpath(".//tr")
#
#         # 默认第一条
#         firstTd = trs[0].find_elements_by_xpath(".//td")
#         # print(firstTd)
#         a = firstTd[2].find_elements_by_xpath("./a")[0].get_attribute("href")
#         # 输出所有href
#         # count=0
#         # for tr in trs:
#         #     print(count)
#         #     #获取链接位置
#         #     tds = tr.find_elements_by_xpath(".//td")
#         #     a=tds[2].find_elements_by_xpath("./a")[0]
#         #     print(sectionResource(a))
#         #     #print(sectionResource(tds[2]))
#         #     count=count+1
#         # 点击进入公司明细页面
#         browser.get(a)
#         wait.until(EC.presence_of_all_elements_located)
#         # pageResource(browser)
#
#         return browser, wait, resultNum


# @server.route('/checkCode',methods=['post'])#只有在函数前加上@server.route (),这个函数才是个接口，不是一般的函数
# def checkCode():
#     global browser
#     code = flask.request.values.get('code')
#     if code:
#         flag=checkVerifiedCode(code)
#         if flag == -1:
#             print("verifiedCode error")
#
#         elif flag == -2:
#             print("net error o verifiedCode error")
#
#         else:
#             try:
#                 items = doScrapyForOneKey(key)
#                 if items == 0:
#                     print("no result list")
#
#                 elif items == -1:
#                     print("no exact result")
#
#                 else:
#                     res = {'msg': '查询成功', 'data': items}  # 1001表示必填接口未填
#
#             except chromeError as e:
#                 print(e.with_traceback())
#                 print(e.errorinfo)
#                 browser.close()
#                 res = {'msg': e.errorinfo, 'msg_code': items}
#
#             except netError as e:
#                 print(e.with_traceback())
#                 print(e.errorinfo)
#                 browser.close()
#                 res = {'msg': e.errorinfo, 'msg_code': items}
#
#             except codeError as e:
#                 print(e.with_traceback())
#                 print(e.errorinfo)
#                 browser.close()
#                 res = {'msg': e.errorinfo, 'msg_code': items}
#
#             except TimeoutException as e:
#                 print(e.with_traceback())
#                 print(e.msg)
#                 browser.close()
#                 res = {'msg': e.errorinfo, 'msg_code': items}
#
#             except Exception as e:
#                 print(e.with_traceback())
#                 print(e.args)
#                 browser.close()
#                 res = {'msg': e.errorinfo, 'msg_code': items}
#     else:
#         res = {'msg': '必填字段未填，请查看接口文档', 'msg_code': 1001}  # 1001表示必填接口未填
#     return json.dumps(res, ensure_ascii=False)
#
# server.run(port=7777,debug=True,host='localhost')
#
#





