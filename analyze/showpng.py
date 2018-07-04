import matplotlib.pyplot as plt



l = [
    [1,2,3,4,5,6,7,8,9,0],
    [23,4,3,5,46,7,34,67,8,12]
]
def showBar(dataList2d, xLabel='时间', yLabel='y'):
    x = dataList2d[0]
    y = dataList2d[1]
    plt.bar(x,y)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)


def showLine(dataList2d):
    pass

showBar(l)
plt.show()