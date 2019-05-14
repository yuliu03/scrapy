
# 上市信息--基本信息
import re

# 过滤无用信息
import sys

from scrapy.util.util import myCopy


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