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
    if key in sessionInfo.keys():
        del sessionInfo[key]

#判断seession是否存在
def checkSessionInfo(key):
    if key in sessionInfo.keys():
        return sessionInfo[key]
    else:
        return -1

#test
def hello(request):
    return HttpResponse("Hello world")

#获取x公司内容
def requestInfo(request):
    browser = ""
    wait = ""
    data=json.loads(request.body.decode("utf8"))
    key = data.get("key")
    print(key)

    #infoDic: browser,wait,imgObj
    response,infoDic=requestInfoHttpResponseJson(key,chromeDir,acount,password,loginDir)
    sessionInfo[infoDic["myid"]] = infoDic
    print(response)

    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"  # 加入这行


    return response

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

#更换验证码
def changeCode(request):
    data = json.loads(request.body.decode("utf8"))
    print(request.body)
    print(request.POST)

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


#开始从网上获取
def doScrapy(request):
    data = json.loads(request.body.decode("utf8"))
    print(request.body)
    print(request.POST)
    verifiedCode = data.get("verifiedCode")
    print(verifiedCode)
    myid = data.get("myid")
    print(myid)

    flag,infoDic = checkVerifiedCode(verifiedCode,sessionInfo[myid]["browser"],sessionInfo[myid]["wait"],myid,sessionTime=0.4)
    if flag == -1:
        print("验证码为生成")
    elif flag == -2:
        print("未生成session id")

    else:
        info,flag=doScrapyForOneKey(sessionInfo[myid]["companyCode"],sessionInfo[myid]["browser"],sessionInfo[myid]["wait"])
        if flag == 0:
            print("未找到公司："+sessionInfo[myid]["companyCode"])
        elif flag == -1:
            print("公司名称有误，请核实")
        else:
            print("内容获取成功")
