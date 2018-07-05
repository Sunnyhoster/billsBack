import pandas as pd
from sklearn.neural_network import MLPRegressor
import operator

data_csv = pd.read_csv('./prediction/simulation.csv')

moneyList = list([int(val) for val in data_csv['money']])
typeList = list([int(val) for val in data_csv['type']])
moodList = list([int(val) for val in data_csv['mood']])

def showType(x=typeList, y=moodList):
    x_list = x[:]
    x = [list([val]) for val in x_list]
    rgr = MLPRegressor()
    rgr.fit(x, y)
    x_list = list(set(x_list))
    x = [list([val]) for val in x_list]
    prediction = rgr.predict(x)
    m = len(x_list)
    d = {}
    for i in range(m):
        d[x_list[i]] = prediction[i]
    sorted_x = sorted(d.items(), key=operator.itemgetter(1))
    top3 = []
    bottom3 = []
    for i in range(3):
        top3.append(sorted_x[i][0])
        bottom3.append(sorted_x[-(i + 1)][0])
    return top3, bottom3


def showMoney(x=typeList, y=moneyList):
    x_list = x[:]
    x = [list([val]) for val in x_list]
    rgr = MLPRegressor()
    rgr.fit(x, y)
    x_list = list(set(x_list))
    x = [list([val]) for val in x_list]
    prediction = rgr.predict(x)
    d = {}
    for i in range(len(x)):
        d[x_list[i]] = str(int(prediction[i]))
    return d

