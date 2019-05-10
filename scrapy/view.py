from django.http import HttpResponse, JsonResponse
from scrapy import *
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world")

def requestInfo(request):
    browser = ""
    wait = ""
    chromeDir = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"  # 这里是你的驱动的绝对地址
    # firefoxDir="D:/firefox/geckodriver.exe"
    loginDir = "https://www.qichacha.com/user_login"
    acount = "13958127726"
    password = "87096927"

    print(request.body)
    print(request.POST)
    data=json.loads(request.body.decode("utf8"))
    print(data)
    key = data.get("key")
    print(key)
    response,infoDic=requestInfoHttpResponseJson(browser,wait,key,chromeDir,acount,password,loginDir)
    print(response)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"  # 加入这行
    return response

def renderHtml(request):
    data = json.loads(request.body.decode("utf8"))
    print(data)
    key = data.get("key")
    print(key)
    data,infoDic=requestInfo( browser,wait,key,chromeDir,acount,password,loginDir)
    if data['msg_code']==1001:
        print(data['data'])
    context = {}
    #context['hello'] = 'hidden'
    context['hello'] = 'form-group col-md-6'
    context['img'] = data['data']
    return render(request, 'index.html', context)

def changeCode(request):
    print(request.body)
    print(request.POST)
    response = changVerifiedCode(imgObj)
    print(response)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"  # 加入这行

    return response