import matplotlib.pyplot as plt
import time


l = [
    [0,1,2,3,4,5,6,7,8,9],
    [23,4,3,5,46,7,34,67,8,12]
]
color = ['red','blue','green','gray','black','yellow','purple','orange']

def showBar(dataList2d, xLabel='x', yLabel='y',color='blue'):
    x = dataList2d[0]
    y = dataList2d[1]
    plt.bar(x,y,fc=color)
    plt.xlabel(xLabel,size=15)
    plt.ylabel(yLabel,size=15)
    plt.title('bar',size=30)


def showLine(dataList2d, xLabel='x', yLabel='y',color='blue'):
    x = dataList2d[0]
    y = dataList2d[1]
    plt.plot(x,y,color=color,linewidth=5)
    plt.xlabel(xLabel, size=15)
    plt.ylabel(yLabel, size=15)
    plt.title('line', size=30)

def showPie(dataList2d):
    x = dataList2d[0]
    y = dataList2d[1]
    plt.pie(x=y, labels=x, shadow=True, autopct='%2.1f', pctdistance=0.8)
    plt.title('pie', size=30)


def savePng(dataList2d, filename, type, xLabel='x', yLabel='y', color='blue'):
    if type == 'bar':
        showBar(dataList2d, xLabel=xLabel, yLabel=yLabel, color=color)
    elif type == 'line':
        showLine(dataList2d, xLabel=xLabel, yLabel=yLabel, color=color)
    elif type == 'pie':
        showPie(dataList2d)
    plt.savefig('./BillsApp/analyze/images/'+filename+'.png')

