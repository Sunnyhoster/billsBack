from __future__ import unicode_literals
from django.db import models
import pandas as pd
import random

# , on_delete=models.CASCADE
class UserInfo(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    sex=models.CharField(max_length=30)
    age=models.CharField(max_length=30)


# Create your models here.
class OnesBills(models.Model):
    time = models.CharField(max_length=30)
    money = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)
    mood = models.CharField(max_length=30)
    host = models.ForeignKey("UserInfo", on_delete=models.CASCADE)


#1代表成功，0代表出错

#增加用户信息
def addUser(username,password,sex,age):
    try:
        #UserInfo.objects.create(username=username, password=password, sex=sex, age=age)
        return 1
    except Exception as e:
        return 0

# a=addUser('people2','123','女','12')
# print(a)


#增加消费记录
def addBills(time,money,type,remark,mood,username):
    try:
        OnesBills.objects.create(time=time, money=money, type=type, remark=remark, mood=mood,
                                 host=UserInfo.objects.get(username=username))
        return 1
    except Exception as e:
        return 0

# a=addBills('20171705','10','吃饭','午餐','1','yang')
# print(a)

#根据用户名删除用户
def deleteUser(username):
    try:
        # user=UserInfo.objects.get(username=username)
        UserInfo.objects.filter(id='80').delete()
        return 1
    except Exception as e:
        return 0

# a=OnesBills.objects.get(id=822).delete()
# print(a)

#根据删除消费记录
def deleteBills(time,money,type,username):
    try:
        UserInfo.objects.get(time=time, money=money, type=type, username=username).delete()
        return 1
    except Exception as e:
        return 0


# 修改账单
def changeBills(username, time, money, type, new_money, new_type, new_remark):
    try:
        user = UserInfo.objects.get(username=username)
        bills= OnesBills.objects.filter(time=time, money=money, type=type)  # 查询一条你要更新的数据
        for bill in bills:
            if bill.host_id==user.id:
                if new_money:
                    bill.money = new_money  # 赋值给你要更新的字段
                if new_type:
                    bill.type = new_type
                if new_remark:
                    bill.remark = new_remark
                bill.save()  # 保存
        return 1
    except Exception as e:
        return 0

# a=changeBills('m','20180701','7','2','NEW','NEW','NEW')
# print(a)


#根据月份查询
def searchBills(time,username):
    try:
        # user = UserInfo.objects.get(username=username)
        # OnesBills.objects.filter(host_id=2,time__contains=time)  # 查询,host_id=user.id ,time__contains=time

        i=0
        bills_time=OnesBills.objects.filter(time__contains=time)
        bills_list = []
        for bill in bills_time:
            if bill.host_id==2:
                dict = {}
                dict['time'] = bill.time
                dict['money']= bill.money
                dict['type'] = bill.type
                dict['remark']=bill.remark
                dict['mood']=bill.mood
                bills_list.append(dict)
        return bills_list
    except Exception as e:
        return 0

# a=searchBills('201807','ldl')
# print(a)


#判断用户是否存在
def exist(username):
    try:
        UserInfo.objects.filter(username=username)
        return 1
    except Exception as e:
        return 0

#根据用户名查询用户所有信息

'''
数据初始化
data_simulation = pd.read_csv('./prediction/simulation.csv')
data_user=pd.read_csv('./prediction/users.csv')
timeList = data_simulation['time']
moneyList = data_simulation['money']
typeList = data_simulation['type']
moodList = data_simulation['mood']
remarkList = data_simulation['remark']
usernameList= data_user['username']
passwordList=data_user['password']
sexList=data_user['sex']
ageList=data_user['age']

m = len(timeList)
n=len(usernameList)



for i in range(m):
    addPeople=UserInfo(
        username=usernameList[i],password=passwordList[i],sex=sexList[i],age=ageList[i]
    )
    addPeople.save()

for i in range(m):
    r=random.randint(1, n)
    addBills=OnesBills(
      time=timeList[i],money=moneyList[i],type=typeList[i],mood=moodList[i],remark=remarkList[i],host=UserInfo.objects.get(id=r)
    )
    addBills.save()
'''



