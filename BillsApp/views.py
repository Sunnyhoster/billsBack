from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 登录函数
# 方法——post
# views-/login
# 用户名——username
# 密码——password
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password', None)
        if username and password:
            pass
        else:
            return HttpResponse('ERROR!')
    else:
        return HttpResponse('ERROR!')


# 注册函数
# 方法——post
# views-/register
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
            pass
        else:
            return HttpResponse('ERROR!')
    else:
        return HttpResponse('ERROR!')

# 增删改查

# 查询账单
# 方法——get
# views-/bill/list
# | 参数 | 说明           | 默认 | 是否必须 |
# | ---- | ------------- | ----| --------|
# | time | 月份，按月份查询| 25   | 是      |
def getBills(request):
    if request.method == 'GET':
        time = request.GET.get('time', None)
        if time:
            pass
        else:
            return HttpResponse('ERROR!')
    return HttpResponse('ERROR!')

# 新增账单
# 方法-post
# # views-/bill_list/new_bill
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
            pass
        else:
            return HttpResponse('ERROR!')
    else:
        return HttpResponse('ERROR!')

# 修改账单
# 方法-post
# views-/bill_list/update_bill
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
            pass
        else:
            return HttpResponse('ERROR!')
    else:
        return HttpResponse('ERROR!')

# 删除账单
# 方法-post
# views-/bill-list/delete_bill
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
            pass
        else:
            return HttpResponse('ERROR!')
    else:
        return HttpResponse('ERROR!')


