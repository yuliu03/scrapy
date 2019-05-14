#写入默认内容，用于未查到信息结果
from telnetlib import EC


def defaultWrite(outputDir,info):
    f = open(outputDir, 'a+',encoding='utf-8')
    for sql in info:
        f.write(sql +'\n')  # 加\n换行显示

    f.write("end" + '\n')  # 加\n换行显示
    f.close()

# 将字符串写入tmp文本
def myCopy(str):
    tmp = open("C:/Users/admin/Desktop/tmp1.txt", 'a+', encoding='utf-8')
    tmp.write(str)
    tmp.close()


# 查看所有页面源代码
def pageResource(browser, wait):
    wait.until(EC.presence_of_all_elements_located)
    html = browser.find_element_by_xpath("//*").get_attribute("outerHTML")
    print(html)


# 查看某段源代码
def sectionResource(section):
    print(section.get_attribute("outerHTML"))
    print("//////////////////")

# 测试输出
def testPrint(inf):
    print("++++++++++++++++++++")
    print(inf)
    print("++++++++++++++++++++")

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
