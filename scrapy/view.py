from django.http import HttpResponse, JsonResponse
from scrapy import *
from django.shortcuts import render
import uuid

chromeDir = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 这里是你的驱动的绝对地址
# firefoxDir="D:/firefox/geckodriver.exe"
loginDir = "https://www.qichacha.com/user_login"
acount = "13958127726"
password = "87096927"

sessionInfo={}


#删除seesion 内容
def delDict(key):
    global sessionInfo
    if key in sessionInfo.keys():
        del sessionInfo[key]

#判断seession是否存在
def checkSessionInfo(myid):
    global sessionInfo
    if myid in sessionInfo.keys():
        return sessionInfo[myid]
    else:
        return None

#获取x公司菜单内容
def requestMenuInfo(request):
    global sessionInfo

    browser = ""
    wait = ""
    data=json.loads(request.body.decode("utf8"))
    key = data.get("key")
    print(key)

    myid = data.get("myid")
    print(myid)

    response = findInLocalDB(key)
    if response == None: #如果本地没有，就找网页上的
        if checkSessionInfo(myid) == None:
            # infoDic: browser,wait,imgObj
            response,infoDic=requestInfoFromWeb(key,chromeDir,acount,password,loginDir)
            if not infoDic=={}:
                sessionInfo[infoDic["myid"]] = infoDic
                print("info has found in local db")
        else:
            print("直接在web搜索框里找")

    print(response)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"  # 加入这行


    return response

#获取公司内容根据表名称
def getInfoByCompanyName(request):
    global sessionInfo

    data = json.loads(request.body.decode("utf8"))
    companyName = data.get("companyName")
    tableName = data.get("tableName")
    if companyName ==None or tableName == None:
        print("companyName ==None or tableName == None")
        res = {'msg': '失败', 'msg_code': 1000, 'data': None}  # 1001表示失败,但是没有内容
        response=HttpResponse(json.dumps(res, ensure_ascii=False))
    else:
        response = getDetailInfo(companyName,tableName)
    print(response)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"  # 加入这行

    return response

#更换验证码
def changeCode(request):
    global sessionInfo

    data = json.loads(request.body.decode("utf8"))
    myid = data.get("myid")
    print(myid)

    oldInfoDic = sessionInfo[myid]
    response,newinfoDic = changVerifiedCode(oldInfoDic)

    print(response)
    sessionInfo[myid] = newinfoDic
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"  # 加入这行

    return response


#接受验证码，判断
def checkCode(request):
    global sessionInfo

    data = json.loads(request.body.decode("utf8"))
    print(request.body)
    print(request.POST)
    verifiedCode = data.get("verifiedCode")
    print(verifiedCode)
    myid = data.get("myid")
    print(myid)

    response,infoDic = checkVerifiedCode(verifiedCode,sessionInfo[myid]["browser"],sessionInfo[myid]["wait"],myid,sessionTime=0.4)
    # if flag == -1:
    #     print("验证码为生成")
    # elif flag == -2:
    #     print("未生成session id")

    print(response)
    sessionInfo[myid] = infoDic
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"  # 加入这行

    return response


#开始从网上获取
def doScrapy(request):
    global sessionInfo

    data = json.loads(request.body.decode("utf8"))
    print(request.body)
    print(request.POST)
    verifiedCode = data.get("verifiedCode")
    print(verifiedCode)
    myid = data.get("myid")
    print(myid)

    # flag,infoDic = checkVerifiedCode(verifiedCode,sessionInfo[myid]["browser"],sessionInfo[myid]["wait"],myid,sessionTime=0.4)
    # if flag == -1:
    #     print("验证码为生成")
    # elif flag == -2:
    #     print("未生成session id")
    #
    # else:
    info,flag=doScrapyForOneKey(sessionInfo[myid]["companyCode"],sessionInfo[myid]["browser"],sessionInfo[myid]["wait"])
    if flag == 0:
        print("未找到公司："+sessionInfo[myid]["companyCode"])
    elif flag == -1:
        print("公司名称有误，请核实")
    else:
        print("内容获取成功")



#########test function###########
#test
def renderHtml(request):
    browser=""
    wait=""
    data = json.loads(request.body.decode("utf8"))
    print(data)
    key = data.get("key")
    print(key)
    data,infoDic=requestInfoScrapy(key,chromeDir,acount,password,loginDir)
    if data['msg_code']==1001:
        print(data['data'])
    context = {}
    #context['hello'] = 'hidden'
    context['hello'] = 'form-group col-md-6'
    context['img'] = data['data']
    return render(request, 'index.html', context)
#test
def hello(request):
    return HttpResponse("Hello world")