from django.http import HttpResponse, JsonResponse
from scrapy import *
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world")

def requestInfoHttpResponseJson1(request):
    print(request.body)
    print(request.POST)
    data=json.loads(request.body.decode("utf8"))
    print(data)
    key = data.get("key")
    print(key)
    response=requestInfoHttpResponseJson(key)
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
    data=requestInfo(key)
    if data['msg_code']==1001:
        print(data['data'])
    context = {}
    #context['hello'] = 'hidden'
    context['hello'] = 'form-group col-md-6'
    context['img'] = data['data']
    return render(request, 'index.html', context)