import re
import sys
import time

import json
import pymysql
import os,django
from django.http import HttpResponse
import xlrd
from xlutils.copy import copy
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import flask,json
import os

from selenium.webdriver.support.wait import WebDriverWait

# 初始化公司名称，用于记录异常
companyCode = "null"


# chrome浏览器异常
class chromeError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


# 网络异常
class netError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo

# 拼装sql数据异常
class sqlError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo

# 验证码失败提示定位
class codeError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


# sessionId生成失败
class sessionIdError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


# 验证码成功
class okException(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


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



# 根据中文名字获取英文字段
def getEnglishName(chinese):
    if ('基本信息' == chinese):
        return 'basic_info'
    elif ('工商信息' == chinese):
        return 'basic_infoGS'
    elif ('股东信息' == chinese):
        return 'shareholder_info'
    elif ('主要人员' == chinese):
        return 'main_staff'
    elif ('变更记录' == chinese):
        return 'change_log'
    elif ('最终受益人' == chinese):
        return 'ultimate_beneficiary'
    elif ('控股企业' == chinese):
        return 'holding_company'
    elif ('上市信息' == chinese):
        return 'ipo_info'
    elif ('重要人员' == chinese):
        return 'important_person'
    elif ('十大股东' == chinese):
        return 'top_ten_shareholders'
    elif ('公司高管' == chinese):
        return 'company_executives'
    elif ('经营状况' == chinese):
        return 'run_state'
    elif ('税务信用' == chinese):
        return 'tax_credit'
    elif ('进出口信用' == chinese):
        return 'import_and_export_credit'
    elif ('经营风险' == chinese):
        return 'run_risk'
    elif ('股权出质' == chinese):
        return 'equity'
    elif ('行政处罚 [工商局]' == chinese):
        return 'administrative_penalties'
    elif ('企业发展' == chinese):
        return 'companyDev'
    elif ('股东（发起人）出资信息' == chinese):
        return 'shareholder_sponsor'
    elif ('对外投资信息' == chinese):
        return 'foreign_investment_information'
    elif ('历史信息' == chinese):
        return 'history_info'
    elif ('历史对外投资' == chinese):
        return 'historical_foreign_investment'
    elif ('历史股东' == chinese):
        return 'historical_shareholder'
    elif ('历史被执行人' == chinese):
        return 'historical executor'
    elif ('历史失信被执行人' == chinese):
        return 'historical_loss_of_trustee'
    elif ('法律诉讼' == chinese):
        return 'legal_action'
    elif ('开庭公告' == chinese):
        return 'opening_notice'
    elif ('法院公告' == chinese):
        return 'court_notice'

    # 记录内容至本地文本


# 将字符串写入tmp文本
def myCopy(str):
    tmp = open("C:/Users/admin/Desktop/tmp1.txt", 'a+', encoding='utf-8')
    tmp.write(str)
    tmp.close()


# 测试输出
def testPrint(inf):
    print("++++++++++++++++++++")
    print(inf)
    print("++++++++++++++++++++")


def get_track(distance):  # distance为传入的总距离
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0

    while current < distance:
        if current < mid:
            # 加速度为2
            a = 2
        else:
            # 加速度为-2
            a = -3
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track


def move_to_gap(slider, tracks, browser):  # slider是要移动的滑块,tracks是要传入的移动轨迹
    ActionChains(browser).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(browser).release().perform()

# 查看所有页面源代码
def pageResource(browser, wait):
    wait.until(EC.presence_of_all_elements_located)
    html = browser.find_element_by_xpath("//*").get_attribute("outerHTML")
    print(html)

def connectDB():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "scrapy", charset='utf8')
    return db

def closeDB(db):
    # 关闭数据库连接
    db.close()

# 查看某段源代码
def sectionResource(section):
    print(section.get_attribute("outerHTML"))
    print("//////////////////")

def changVerifiedCode(img):
    # 验证码更新
    global browser
    ActionChains(browser).click(img).perform()
    time.sleep(0.5)
    # 获取验证图片，base64编码，可以通过html展示
    img = browser.find_element_by_xpath("//div[@id='nc_1__imgCaptcha_img']/img")
    verifiedCode = img.get_attribute("src")
    return verifiedCode


#判断验证码信息，如果正确，点击进入搜索页面
def checkVerifiedCode(code,sessionTime=0.4):
        try:
            global browser
            global wait

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
        return flag

def requestLogin():
    global browser
    global wait
    global chromeDir
    global loginDir
    global acount
    global password

    searchDir = chromeDir

    browser = webdriver.Chrome(searchDir)

    try:
        # 设置浏览器需要打开的url
        url = loginDir
        browser.get(url)

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
            return verifiedCode


        except sessionIdError as e:
            raise sessionIdError(e.errorinfo)

        except codeError as e:
            raise codeError(e.errorinfo)

    except TimeoutException as e:
        raise TimeoutException(e.msg)

# 搜索栏搜索公司信息
def searchOne( companyCode):
    try:
        global browser
        global wait

        # 等待搜索框出现
        wait.until(EC.presence_of_element_located((By.ID, "searchkey")))

        # 填写搜索内容
        search = browser.find_element_by_id("searchkey")
        search.send_keys(companyCode)

        # 定位搜索按钮并且点击触发
        doSearch = browser.find_element_by_id("V3_Search_bt")
        doSearch.click()


    except netError as e:
        raise netError("网络不稳定，请重新连接")


def selectForOne(companyCode):
    global wait
    global browser
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
        return resultNum

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
        a = firstTd[2].find_elements_by_xpath("./a")[0].get_attribute("href")

        # 点击进入公司明细页面
        browser.get(a)
        wait.until(EC.presence_of_all_elements_located)
        # pageResource(browser)

        return resultNum

# 从搜索结果中选择公司，返回相关链接
def select(wait, browser, companyCode):
    # resultNum 判断搜索结果数量
    resultNum = '0'

    # 等待结果数量显示
    # pageResource(browser,wait)
    # wait.until(EC.presence_of_element_located((By.ID, "//*[@id='countOld']")))
    # 获取结果数量
    num = browser.find_element_by_xpath("//*[@id='countOld']/span").text
    if num == '0':  # 判断是否有结果
        print("no result: " + "[result number: " + num + "]")

        return browser, wait, resultNum

    resultName = browser.find_element_by_xpath("//*[@id='search-result']/tr[1]/td[3]/a").text
    if resultName != companyCode:  # 判断字段是否绝对一样
        print("[companyCode: " + companyCode + "]"
              + "result company name: " + resultName)
        return browser, wait, resultNum

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
        a = firstTd[2].find_elements_by_xpath("./a")[0].get_attribute("href")
        # 输出所有href
        # count=0
        # for tr in trs:
        #     print(count)
        #     #获取链接位置
        #     tds = tr.find_elements_by_xpath(".//td")
        #     a=tds[2].find_elements_by_xpath("./a")[0]
        #     print(sectionResource(a))
        #     #print(sectionResource(tds[2]))
        #     count=count+1
        # 点击进入公司明细页面
        browser.get(a)
        wait.until(EC.presence_of_all_elements_located)
        # pageResource(browser)

        return browser, wait, resultNum

# 上市信息--基本信息
def ipoInfo_basic(sec):
    tds = sec.find_all('tbody')[0].find_all('td')
    dic = tableInfo(tds)
    return dic

# 上市信息
def ipoInfo(soup):
    ss = soup.findAll('section', {'class': re.compile('panel')})

    # 初始化上市信息页面内容储存空间
    ipoInfo = list()
    for sec in ss:
        try:
            dic = None
            if (sec.div.h3.text.strip() == "重要人员"):
                print("重要人员")
                dic = ipoInfo_basic(sec)
            elif (sec.div.h3.text.strip() == "十大股东"):
                print("十大股东")
                dic = actionInfo(sec)
            elif (sec.div.h3.text.strip() == "公司高管"):
                print("公司高管")
                dic = actionInfo(sec)

            # 将内容插入上市信息页面内容储存空间
            if dic != None:
                ipoInfo.append((sec.div.h3.text.strip(), dic))
        except AttributeError:
            pass
    return ipoInfo

# 基本信息模块信息爬取
def rowTableInfo(sec):
    tbody = sec.find('tbody')

    trs = tbody.find_all('tr', recursive=False)

    inf = tableInfo2(trs)

    return inf

# 获取经营状况页面内容
def runState(soup):
    ss = soup.findAll('section', {'class': re.compile('panel')})

    # 初始化经营状况页面内容储存空间
    runStateInfo = list()

    for sec in ss:
        try:
            dic = None
            if (sec.div.h3.text.strip() == "税务信用"):
                print("税务信用")
                dic = actionInfo(sec)
            if (sec.div.h3.text.strip() == "进出口信用"):
                print("进出口信用")
                dic = actionInfo(sec)

            # 将内容插入经营状况页面内容储存空间
            if dic != None:
                runStateInfo.append((sec.div.h3.text.strip(), dic))
        except AttributeError:
            pass

    return runStateInfo

# 获取经营风险页面内容
def runRisk(soup):
    # print(soup)
    ss = soup.findAll('section', {'class': re.compile('panel')})

    # 初始化经营风险页面内容储存空间
    runRiskInfo = list()
    for sec in ss:
        try:
            dic = None
            if (sec.div.h3.text.strip() == "股权出质"):
                print("股权出质")
                dic = actionInfo(sec)
            elif (sec.div.h3.text.strip() == "行政处罚 [工商局]"):
                print("行政处罚 [工商局]")
                dic = actionInfo(sec)

            # 将经营风险信息插入信息储存表
            if dic != None:
                runRiskInfo.append((sec.div.h3.text.strip(), dic))

        except AttributeError:
            pass

    return runRiskInfo

# 获取企业发展页面内容
def companyDev(soup):
    reportSeccion = soup.find('section', {'id': 'report'})

    if reportSeccion == None:
        return None

    # 获取多年的年报，时间越晚的，排位越后
    ss = reportSeccion.findAll('div', {'class': re.compile('tab-pane')})

    # 默认只对最近一年的操作
    recentlyReport = ss[0]

    # 获取所有抬头代码
    h3s = recentlyReport.findAll('h3')

    # 获取所有内容
    tables = recentlyReport.findAll('table')

    if len(h3s) != len(tables):
        raise RuntimeError("字段内容数量是否和字段名称数量不一致")

    else:

        # 初始化企业发展页面内容储存空间
        companyDevInfo = list()

        count = 0
        for x in h3s:
            dic = None
            if x.text.strip() == "股东（发起人）出资信息":
                print("股东（发起人）出资信息")
                dic = actionInfo(tables[count])

            elif x.text.strip() == "对外投资信息":
                print("对外投资信息")
                dic = actionInfo(tables[count])

            count = count + 1

            # 将企业发展信息插入信息储存表
            if dic != None:
                companyDevInfo.append((x.text.strip(), dic))

        return companyDevInfo

# 获取知识产权页面内容(暂时无需求)
def IntellectualPro(soup):
    pass

# 获取历史信息页面信息
def historyInfo(soup):
    ss = soup.findAll('section', {'class': re.compile('panel')})

    # 初始化历史信息页面内容储存空间
    historyInfo = list()

    for sec in ss:
        try:
            dic = None
            if (sec.div.h3.text.strip() == "历史对外投资"):
                print("历史对外投资")
                dic = actionInfo(sec)
            elif (sec.div.h3.text.strip() == "历史股东"):
                print("历史股东")
                dic = actionInfo(sec)
            elif (sec.div.h3.text.strip() == "历史被执行人"):
                print("历史被执行人")
                dic = actionInfo(sec)
            elif (sec.div.h3.text.strip() == "历史失信被执行人"):
                print("历史失信被执行人")
                dic = actionInfo(sec)

            # 将企业历史信息插入信息储存表
            if dic != None:
                historyInfo.append((sec.div.h3.text.strip(), dic))

        except AttributeError:
            pass

    return historyInfo

# 法律诉讼信息内容选择
def legalAction(soup):
    ss = soup.findAll('section', {'class': re.compile('panel b-a')})
    # 初始化法律诉讼信息储存表
    legalInfo = list()
    for sec in ss:
        try:
            dic = None
            if (sec.div.h3.text.strip() == "开庭公告"):
                print("开庭公告")
                dic = actionInfo(sec)
            elif (sec.div.h3.text.strip() == "法院公告"):
                print("法院公告")
                dic = actionInfo(sec)

            # 将信息插入法律诉讼信息储存表
            if dic != None:
                legalInfo.append((sec.div.h3.text.strip(), dic))

        except AttributeError:
            pass

    return legalInfo

# 辅助获取信息模块信息爬取
def actionInfo(sec):
    tbody = sec.find('tbody')

    trs = tbody.find_all('tr', recursive=False)
    try:
        inf = tableInfo2(trs)
        return inf
    except RuntimeError as e:
        print(e.args)
        print(sec)

# 基本信息--工商信息
def basicInfoGS(tr):
    tds = tr.find_all('tbody')[1].find_all('td')
    dic = tableInfo(tds)
    return dic

# 基本信息模块内容选择
def basicInfo(soup):
    ss = soup.findAll('section', {'class': re.compile('panel b-a')})

    # 初始化模块内容储存空间
    businessInfo = list()

    for sec in ss:
        try:
            dic = None
            if (sec.div.h3.text.strip() == "工商信息"):
                print("工商信息")
                dic = basicInfoGS(sec)
            elif (sec.div.h3.text.strip() == "股东信息"):
                print("股东信息")
                dic = rowTableInfo(sec)
            elif (sec.div.h3.text.strip() == "主要人员"):
                print("主要人员")
                dic = rowTableInfo(sec)
            elif (sec.div.h3.text.strip() == "变更记录"):
                print("变更记录")
                dic = rowTableInfo(sec)
            elif (sec.div.h3.text.strip() == "最终受益人"):
                print("最终受益人")
                dic = rowTableInfo(sec)
            elif (sec.div.h3.text.strip() == "控股企业"):
                print("控股企业")
                dic = rowTableInfo(sec)
            # elif (sec.div.h3.text.strip() == "财务简析"):
            #     print("财务简析")
            # print(sec)
            # dic = shareholderInfo(sec)
            # print(dic)
            # elif (sec.div.h3.text.strip() == "同业分析"):
            #     print("同业分析")
            # print(sec)
            # dic = shareholderInfo(sec)
            # print(dic)
            # 将信息插入基础信息表
            if dic != None:
                businessInfo.append((sec.div.h3.text.strip(), dic))
        except AttributeError:
            pass

    return businessInfo

# 用于上下形式的table,数据结构{(字段名),(对应内容)...},字段数量和内容数量保持一致
def tableInfo2(trs):
    # 初始化数据储存列表
    inf = list()

    # 获取所有抬头
    ths = trs[0].find_all('th')

    # 获取字段名称,过滤空格等问题
    names = list()  # 初始化抬头列表
    for name in ths:
        # 方法一：拼接字符串
        # names+='('+name.text.strip().replace("\n", "").replace("\t", "")+')'

        # 方法二：list直接添加
        title = tableInfo2Filter(name.text.strip().replace("\n", "").replace("\t", ""))

        names.append(title)

    # 过滤空格等冗余信息,将字段名称加入数据储存列表
    inf.append(names)

    # 获取字段数量
    nameSize = len(ths)

    # 方法一：（拼接字符串）删除字段名称，获取字段内容
    #############################################
    # del(trs[0])
    # for tr in trs:
    #     value=''
    #     tds=tr.find_all('td',recursive=False)
    #
    #     #判断是否有内容
    #     if len(tds)>0:
    #         # 初始化内容类数量
    #         valueSize = 0
    #         # 获取每一行信息
    #         for td in tds:
    #             tmp = ''
    #             try:
    #                 tmp += td.find('h3').text.strip().replace("\n", "").replace("\t", "")
    #             except:
    #                 tmp += td.text.strip().replace("\n", "").replace("\t", "")
    #
    #             if (tmp != ''):
    #                 # 字段内容类数量加一
    #                 valueSize += 1
    #                 value += '(' + tmp + ')'
    #
    #         # print("value: ")
    #         # print(tableInfo2Filter(value))
    #         # print("-----------------")
    #
    #         # 过滤空格等冗余信息,将字段内容加入list
    #         inf.append(tableInfo2Filter(value))
    #
    #         # 每获取一行信息，验证字段内容数量是否和字段名称数量一致
    #         if (nameSize != valueSize):
    #             print(ths)
    #             print("/////")
    #             print(tds)
    #             print("/////")
    #             print(inf)
    #             raise RuntimeError("字段内容数量是否和字段名称数量不一致")
    #             break
    #############################################

    # 方法二：（list直接添加）删除字段名称，获取字段内容
    ##############################################
    del (trs[0])
    for tr in trs:
        value = list()  # 初始化内容列表
        tds = tr.find_all('td', recursive=False)

        # 判断是否有内容
        if len(tds) > 0:
            # 初始化内容类数量
            valueSize = 0
            # 获取每一行信息
            for td in tds:
                tmp = ''
                try:
                    if td.find('h3').text.strip().replace("\n", "").replace("\t", "") != "":
                        tmp += '-'
                    else:
                        tmp += td.find('h3').text.strip().replace("\n", "").replace("\t", "")
                except:
                    tmp += td.text.strip().replace("\n", "").replace("\t", "")

                if (tmp != ''):
                    # 字段内容类数量加一
                    valueSize += 1
                    value.append(tableInfo2Filter(tmp))

            # 过滤空格等冗余信息,将字段内容加入数据储存列表
            inf.append(value)

            # 每获取一行信息，验证字段内容数量是否和字段名称数量一致
            if (nameSize != valueSize):
                print(ths)
                print("/////")
                print(tds)
                print("/////")
                print(inf)
                myCopy(companyCode.__str__() + "\n" + tds.__str__() + "\n" + inf.__str__())
                print("字段内容数量是否和字段名称数量不一致")
                pass
    ###############################################

    # 数字1代表表格是上下类型
    return (1, inf)

# 最基础信息
def topInf(soup):
    # 获取公司名
    try:
        conpanyname = soup.find('div', {'class': 'row title jk-tip'}).h1.text.strip()
    except AttributeError:
        sys.exit('获取不了目标页面内容,爬虫自动退出,请检查目标页面是否正常打开或者自动跳转到首页')
    # 获取电话、邮箱、官网、公司地址信息
    row = soup.find('div', {'class': 'dcontent'}).find_all('div', {'class': 'row'})
    for i in row:
        # 判断是否i.find('span',{'class':'cdes'})有内容
        if i.find('span', {'class': 'cdes'}):
            # 判断获取的i.find('span',{'class':'cdes'})是否为电话
            if i.find('span', {'class': 'cdes'}).text.strip() == '电话：':
                try:
                    tel = i.find('span', {'class': 'cvlu'}).span.text.strip()
                except AttributeError:
                    tel = i.find('span', {'class': 'cvlu'}).text.strip()
                # 获取官网
                if i.find('span', {'class': 'cdes'}).find_parent().find_next_sibling().text.strip() == '官网：':
                    try:
                        web = i.find('span', {'class': 'cdes'}).find_parent().find_next_sibling().find_next(
                            'span').a.find_next('a').text.strip()
                    except AttributeError:
                        web = i.find('span', {'class': 'cdes'}).find_parent().find_next_sibling().find_next(
                            'span').text.strip()
            # 判断获取的i.find('span',{'class':'cdes'})是否为邮箱
            if i.find('span', {'class': 'cdes'}).text.strip() == '邮箱：':
                try:
                    email = i.find('span', {'class': 'cvlu'}).text.strip()
                except AttributeError:
                    email = '暂无'
                # 获取地址
                if i.find('span', {'class': 'cdes'}).find_parent().find_next_sibling().text.strip() == '地址：':
                    try:
                        address = i.find('span', {'class': 'cdes'}).find_parent().find_next_sibling().find_next(
                            'span').a.text.strip()
                    except AttributeError:
                        address = i.find('span', {'class': 'cdes'}).find_parent().find_next_sibling().find_next(
                            'span').text.strip()

# 用于左右形式的table
def tableInfo(tds):
    flag = 'key'
    inf = list()
    for td in tds:
        if (flag == 'key'):
            key = td.text.strip().replace("\n", "").replace("\t", "")
            flag = 'value'
        else:
            value = td.text.strip().replace("\n", "").replace("\t", "")
            flag = 'key'
            # add新键值对
            inf.append((key, tableInfo2Filter(value)))

    # 数字0代表左右表格
    return (0, inf)

# 过滤无用信息
def tableInfo2Filter(l):
    patterns = list()

    # 删除冗余内容
    patterns.append(re.compile(r'(查看最终受益人>)'))
    patterns.append(re.compile(r'他投资(\d+)家公司(\s*)>'))
    patterns.append(re.compile(r'他关联(\d+)家公司(\s*)>'))
    patterns.append(re.compile(r'查看地图'))
    patterns.append(re.compile(r'附近公司'))

    # 过滤多余空格
    patterns.append(re.compile(r'(\s+)'))

    clearInf = l
    for pattern in patterns:
        # 根据条件进行处理
        clearInf = re.sub(pattern, '', clearInf)

    return clearInf

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
def beginNav():
    global browser
    global wait

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
    sheetNames = list()
    sheetKeysValues = list()  # list<tableType,keys,values,tableName>
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

            sheetNames.append(tableName)

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

                sheetKeysValues.append((tableType, keys, values, tableName))

            # 判断，数字1为左右类型table
            elif tableType == 0:
                print("table: " + table.__str__())
                for i in table:
                    keys.append(i[0])
                    values.append(i[1])

                # 写死加入公司名称和模块名称，需要保持key和value的位置一致
                keys.append("module_name")
                keys.append("company_name")

                sheetKeysValues.append((tableType, keys, values, tableName))

        print("----------")
        # print("table name: "+item[1][0].__str__())
        # print("----------")
        # print("table type: " + item[1][1][0].__str__())
        # print("----------")
        # print("table info: " + item[1][1][1].__str__())

    print(sheetKeysValues)
    print("////////////////")

    # 遍历所有的模块
    for i in sheetKeysValues:
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

def doScrapyForOneKey(key):
        global browser
        global wait
        # 第一个公司，名称
        companyCode = key

        ###############################
        # 进入主页面
        ###############################
        # 搜索公司信息
        print("-----开始搜索-----")
        searchOne(companyCode)
        print("-----结束搜索-----")

        ###############################
        # 进入主搜索结果列表页面
        ###############################
        print("-----开始对搜索结果进行操作-----")
        resultNum = selectForOne(companyCode)
        print("-----结束对搜索结果进行操作-----")
        ###############################
        # 获取所有菜单链接
        ###############################

        if resultNum == '0':
            return '0'

        if resultNum == '-1':
            return '-1'


        print("-----开始对公司信息目录进行操作-----")
        items = beginNav()
        print("-----结束对公司信息目录进行操作-----")
        print("===========写入内容至本地文本=================")
        #writeResult(output, items, companyCode)

        #获取sql语句拼装信息
        db = connectDB()
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        affectRows = cursor.execute("select english,chinese from dictionary")
        print(affectRows)
        result = cursor.fetchone()
        dic = dict()
        while result != None:
            dic[result[1]] = result[0]
            print(result, cursor.rownumber)
            result = cursor.fetchone()

        #插入内容至db
        insertInfo(items,companyCode,dic)

        db = closeDB(db)
        #返回内容
        return items

def preBegin():
    global browser
    global wait
    global key
    global chromeDir
    global acount
    global password
    global loginDir
    global key

    # login
    print("-----开始登录-----")
    verifiedCode = requestLogin()
    print("-----结束登录-----")

    return verifiedCode

    #return doScrapyForOneKey(key,browser, wait)

########################################################
browser = ""
wait = ""
key = ""
img = ""
chromeDir = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 这里是你的驱动的绝对地址
# firefoxDir="D:/firefox/geckodriver.exe"
loginDir = "https://www.qichacha.com/user_login"

acount = "13958127726"
password = "87096927"

#server=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动

def insertDB(db,sql):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    affectRows = cursor.execute(sql)

    if(affectRows<=0):
        raise Exception("affectRows<=0")

    db.commit()

def selectOneSql(sql,db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    affectRows = cursor.execute(sql)
    data = cursor.fetchone()

    db.commit()

    return data,affectRows

def selectAllSql(sql,db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    affectRows = cursor.execute(sql)
    data = cursor.fetchall()

    db.commit()

    return data,affectRows

#判断公司名称是否存在
def checkCompany(key):
    db=connectDB()

    #拼装sql语句
    newkey = "'"+key+"'"
    sql="select company_name from companies where company_name = "+newkey
    data,flag=selectOneSql(sql,db)
    if flag == 1:
        data, flag = selectTableInfo("scrapy", "company_table_info", key)
    closeDB(db)

    return data,flag

#返回字符串逗号分隔，不包括",id,creater,create_time,updater,update_time"
def getAllCols(dbName,tableName):
    db = connectDB()

    sql = "SELECT GROUP_CONCAT(COLUMN_NAME SEPARATOR ',') FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = '" + dbName + "' AND TABLE_NAME = '" + tableName + "'"
    data, flag = selectOneSql(sql, db)
    partToDel = ",id,creater,create_time,updater,update_time"
    requestCols = data[0].strip().replace(partToDel, "")

    closeDB(db)
    return requestCols

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

#写入默认内容，用于未查到信息结果
def defaultWrite(outputDir,info):
    f = open(outputDir, 'a+',encoding='utf-8')
    for sql in info:
        f.write(sql +'\n')  # 加\n换行显示

    f.write("end" + '\n')  # 加\n换行显示
    f.close()

def updateSql(sql,db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    affectRows = cursor.execute(sql)

    db.commit()
    return affectRows

def testx():
    l = list()
    d1 = {}
    d1["a"] = "a"
    d1["a2"] = "a"
    d1["a3"] = "a"

    d2 = {}
    d2["a"] = "a"
    d2["a2"] = "a"
    d2["a3"] = "a"

    d3 = {}
    d3["a"] = "a"
    d3["a2"] = "a"
    d3["a3"] = "a"
    l.append(d1)
    l.append(d2)
    l.append(d3)
    return l
#test
# data,flag=selectTableInfo("scrapy","company_table_info","国网山东平度市供电公司1")
# data,flag=checkCompany("国网山东平度市供电公司")
# print(data)
# print(flag)
#test


#refillCompanyTableInfo("scrapy")



#@server.route('/preBegin',methods=['post'])#只有在函数前加上@server.route (),这个函数才是个接口，不是一般的函数
def requestInfoHttpResponseJson(input):
    global key
    key = input
    if key=="" or key == None:
        res = {'msg': '必填字段未填，请查看接口文档', 'msg_code': 1001}  # 1001表示必填接口未填
    else:
        try:
            print(key)
            data,flag=checkCompany(key)
            if flag >= 1:
                res = {'msg': '信息', 'msg_code': 1000,'data':data}  # 1000表示成功
            else:
                verifiedCode = preBegin()
                res = {'msg': '验证码', 'msg_code': 1000,'data':verifiedCode}  # 1000表示成功
        except netError as e:
            res = {'msg': '网络不稳定', 'msg_code': 1002}  # 1002表示网络错误
            browser.close()

    return HttpResponse(json.dumps(res,ensure_ascii=False))


def requestInfo(input):
    global key
    key = input
    if key=="" or key == None:
        res = {'msg': '必填字段未填，请查看接口文档', 'msg_code': 1003}  # 1003表示必填接口未填
    else:
        try:
            print(key)
            data,flag=checkCompany(key)
            if flag >= 1:
                res = {'msg': '信息', 'msg_code': 1000,'data':data}  # 1000表示成功，返回信息
            else:
                verifiedCode = preBegin()
                res = {'msg': '验证码', 'msg_code': 1001,'data':verifiedCode}  # 1001表示成功,返回验证码
        except netError as e:
            res = {'msg': '网络不稳定', 'msg_code': 1002}  # 1002表示网络错误
            browser.close()
    print(res)
    return res
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





