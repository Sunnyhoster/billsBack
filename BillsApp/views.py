from django.shortcuts import render
from BillsApp.analyze.showpng import *
from django.http import HttpResponse
import json
from BillsApp.analyze.showimage import *
from prediction.showTypeMoney import *

# Create your views here.

# 登录函数
# 方法——post
# path-/login/
# 用户名——username
# 密码——password
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)
        if username and password:
            dict = {'username':username,'password':password}
            jDict = json.dumps(dict)
            return HttpResponse(jDict) # test
        else:
            ditc = {'error':'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error':'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'login.html') # test




# 注册函数
# 方法——post
# path-/register/
# 用户名——username
# 性别——sex
# 年龄——age
# 密码——password
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        sex = request.POST.get('sex', None)
        age = request.POST.get('age', None)
        password = request.POST.get('password', None)
        if username and password:
            dict = {'username':username,'sex':sex,'age':age,'password':password}
            jDict = json.dumps(dict)
            return HttpResponse(jDict) # test
        else:
            dict = {'error':'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'register.html') # test
# 增删改查

# 查询账单
# 方法——get
# path-/bill/list/
# | 参数 | 说明           | 默认 | 是否必须 |
# | ---- | ------------- | ----| --------|
# | time | 月份，按月份查询| 25   | 是      |
def getBills(request):
    if request.method == 'GET':
        time = request.GET.get('time', None)
        if time:
            dict = {'time':time}
            jDict = json.dumps(dict)
            return HttpResponse(jDict) # test
        else:
            dict = {'error':'no time'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        dict = {'error':'not get'}
        jDict = json.dumps(dict)
        return HttpResponse(jDict)

# 新增账单
# 方法-post
# path-/bill_list/new_bill/
# | 字段   | 数据类型 | 说明                  | 是否必须 |
# | ------ | -------- | --------------------- | -------- |
# | time   | string   | 记账时间              | 是       |
# | money  | string   | 金额                  | 是       |
# | type   | string   | 账目类型              | 是       |
# | remark | string   | 备注                  | 否       |
# | mood   | string   | 心情级别(分1、2、3级) | 否       |
def addBills(request):
    if request.method == 'POST':
        time = request.POST.get('time', None)
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        remark = request.POST.get('type', None)
        mood = request.POST.get('mood', None)
        if time and money and type:
            dict = {'time':time,'money':money,'type':type,'remark':remark,'mood':mood}
            jDict = json.dumps(dict)
            return HttpResponse(jDict) # test
        else:
            dict = {'error':'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'addBills.html') # test


# 修改账单
# 方法-post
# path-/bill_list/update_bill/
# | 字段       | 数据类型 | 说明                           | 是否必须 |
# | ---------- | -------- | ------------------------------ | -------- |
# | time       | string   | 记账时间，具体到日             | 是       |
# | money      | string   | 金额                           | 是       |
# | type       | string   | 记账类型                       | 是       |
# | order      | string   | 以上信息相同的账单之中的第几个 | 是       |
# | new_money  | string   | 更新的金额                     | 否       |
# | new_type   | string   | 更新的账目类型                 | 否       |
# | new_remark | string   | 更新的备注                     | 否       |

def updateBills(request):
    if request.method == 'POST':
        time = request.POST.get('time', None)
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        order = request.POST.get('type', None)
        new_money = request.POST.get('new_money', None)
        new_type = request.POST.get('new_type', None)
        new_remark = request.POST.get('new_remark', None)
        if time and money and type and order:
            dict = {'time':time,'money':money,'type':type,'order':order}
            jDict = json.dumps(dict)
            return HttpResponse(jDict) # test
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'updateBills.html') # test


# 删除账单
# 方法-post
# path-/bill-list/delete_bill/
# | 参数  | 说明                         | 是否必须 |
# | ----- | ---------------------------- | -------- |
# | time  | 要删除的账单的时间           | 是       |
# | money | 金额                         | 是       |
# | type  | 账目类型                     | 是       |
# | order | 以上信息相同的账单中的第几个 | 否       |
def deleteBills(request):
    if request.method == 'POST':
        time = request.POST.get('time', None)
        money = request.POST.get('money', None)
        type = request.POST.get('type', None)
        order = request.POST.get('order', None)
        if time and money and type:
            dict = {'time':time,'money':money,'type':type}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)# test
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'deleteBills.html') # test


# 画图并发送
# 方法-post
# path-/image/
# |参数             说明     是否必须   数据类型
# |------------------------------------------
# |filename       返回图片名   是      string
# |coordinate_x   x坐标对象    是      string
# |coordinate_y   y坐标对象    是      string
# |type           数据图类型   是      string
# |color          颜色        否      string
# |date_start     开始日期     是      string
# |date_end       结束日期     是      string
# x,y坐标对象只可从['time','money','type']中选择
# type只可从['bar','line','pie']中选择，分别对应柱状图、折线图、饼图
# color只可从['red','blue','green','gray','black','yellow','purple','orange']中选择，其中饼图color无效，柱状图和折线图必须要color
# date_start 和 date_end 与 time 同一格式
l = [
    [0,1,2,3,4,5,6,7,8,9],
    [23,4,3,5,46,7,34,67,8,12]
]

def sendImage(request):
    if request.method == 'POST':
        filename = request.POST.get('filename', None)
        coordinate_x = request.POST.get('coordinate_x', None)
        coordinate_y = request.POST.get('coordinate_y', None)
        type = request.POST.get('type', None)
        color = request.POST.get('color', None)
        date_start = request.POST.get('date_start', None)
        date_end = request.POST.get('date_end', None)
        if filename and coordinate_x and coordinate_y and type and date_start and date_end:
            if coordinate_x in ['time','money','type'] and coordinate_y in ['time','money','type']:
                if type in ['bar','line','pie']:
                    if type == 'pie':
                        # savePng(dataList2d=?,filename, type, xLabel=coordinate_x, yLabel=coordinate_y, color=color)
                        # return sendImage(filename)
                        savePng(l, filename, type, xLabel = coordinate_x, yLabel = coordinate_y, color = color)
                        return showImage(filename) # test
                    else:
                        if color in ['red','blue','green','gray','black','yellow','purple','orange']:
                            # savePng(dataList2d=?,filename, type, xLabel=coordinate_x, yLabel=coordinate_y, color=color)
                            # return sendImage(filename)
                            savePng(l, filename, type, xLabel=coordinate_x, yLabel=coordinate_y, color=color)
                            return showImage(filename) # test
                        else:
                            dict = {'error': 'color error'}
                            jDict = json.dumps(dict)
                            return HttpResponse(jDict)
                else:
                    dict = {'error': 'type error'}
                    jDict = json.dumps(dict)
                    return HttpResponse(jDict)
            else:
                dict = {'error': 'coordinate error'}
                jDict = json.dumps(dict)
                return HttpResponse(jDict)
        else:
            dict = {'error': 'something absent'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        # dict = {'error': 'not post'}
        # jDict = json.dumps(dict)
        # return HttpResponse(jDict)
        return render(request, 'sendImage.html')
# 消费分析预测
# 方法-get
# path-/prediction/
# 参数：username
# | 字段   | 数据类型 | 说明 |
# | ------ | -------- | ---- |
# | top1 | string   |用户最喜欢的消费类型 |
# | top2 | string   |用户第二喜欢的消费类型 |
# | top3 | string   |用户第三喜欢的消费类型 |
# | bottom1 | string   |用户最不喜欢的消费类型 |
# | bottom2 | string   |用户第二不喜欢的消费类型 |
# | bottom3 | string   |用户第三不喜欢的消费类型 |
# | top1_money | string   |用户最喜欢的消费类型对应金额 |
# | top2_money  | string   |用户第二喜欢的消费类型对应金额 |
# | top3_money  | string   |用户第三喜欢的消费类型对应金额 |
# | bottom1_money | string   |用户最不喜欢的消费类型对应金额 |
# | bottom2_money | string   |用户第二不喜欢的消费类型对应金额 |
# | bottom3_money | string   |用户第三不喜欢的消费类型对应金额 |
def consumePrediction(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if username:
            top3, bottom3 = showType()
            d = showMoney()
            dict = {}
            dict['top1_money'] = d[top3[0]]
            dict['top2_money'] = d[top3[1]]
            dict['top3_money'] = d[top3[2]]
            dict['bottom1_money'] = d[bottom3[0]]
            dict['bottom2_money'] = d[bottom3[1]]
            dict['bottom3_money'] = d[bottom3[2]]
            top3, bottom3 = [str(val) for val in top3], [str(val) for val in bottom3]
            dict['top1'] = top3[0]
            dict['top2'] = top3[1]
            dict['top3'] = top3[2]
            dict['bottom1'] = bottom3[0]
            dict['bottom2'] = bottom3[1]
            dict['bottom3'] = bottom3[2]
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
        else:
            dict = {'error':'no username'}
            jDict = json.dumps(dict)
            return HttpResponse(jDict)
    else:
        dict = {'error':'not get'}
        jDict = json.dumps(dict)
        return HttpResponse(jDict)