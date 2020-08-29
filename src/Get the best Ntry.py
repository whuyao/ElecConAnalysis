from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from sklearn import ensemble
data = pd.read_csv('Data2Train_417.csv')
#data = pd.read_csv('D:\Result\CSVDATA\\test5.csv')
pd.set_option('display.max_columns', None)
X = data[['dis_trainstation','dis_road','dis_river','dis_railway','transportation','slope','Shopping','restaurant','population','nightlight','hotel','hospital','finance','entertainment','enterprise','elevation','education','dailyfacility','community']]
y = data[['SJSJ']]

X_train,X_test,y_train,y_test = train_test_split(X,y.values.ravel())


def getRMES(pred, test):
    for i in range(len(pred)):
        sum_result = (test[i] - pred[i]) * (test[i] - pred[i])
    mse_number = sum_result / len(pred)
    return math.sqrt(mse_number)



def test_DecisionTreeRegressor_depth(X,y, max_val):

    depths = np.arange(1, max_val)
    training_scores = []
    testing_scores = []
    for depth in depths:
        print(depth)
        regr = ensemble.RandomForestRegressor( criterion="mse",oob_score=True,max_features=depth,n_estimators=100)
        regr.fit(X_train, y_train)
        #testing_scores.append(regr.oob_score_)
        print(round(regr.score(X_test,y_test),5).__str__())
        testing_scores.append(regr.score(X_test,y_test))


    ## 绘图
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # ax.plot(depths,training_scores,label="traing score")

    ax.plot(depths, testing_scores, 'd-', label="testing score")

    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    plt.xticks(range(0,20))
    plt.yticks(np.arange(0.55, 0.63,0.005))
    font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 12,
             }
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
    ax.set_xlabel("mtry",font1)
    ax.set_ylabel("模型精度", fontproperties=font)
    #ax.legend(framealpha=0.5,prop={'family' : 'Times New Roman', 'size'   : 12})
    plt.show()



'''
#data = pd.read_csv('E:\CXY\Corrected_DATA\Test_4.csv')
data = pd.read_csv('E:\CXY\Corrected_DATA\Test_0320_2.csv')
pd.set_option('display.max_columns', None)

#X = data[['Log_Enter','Log_Hotel','Log_Meal','Log_Enterprise','Log_Shop','Log_Edu','Log_Econ','Log_Daily','Log_Med','Log_Dis_Railway','Log_Dis_Road']]
X = data[['road','小区','人口密度','公司','交通','教育','金融','购物','医疗','饮食','娱乐','生活设施','旅馆','light','坡度','dis_road','dis_tielu','dis_huochezhan','dis_haiway']]
y = data[['SJSJ_2']]
'''
test_DecisionTreeRegressor_depth(X,y.values.ravel(), max_val=20)