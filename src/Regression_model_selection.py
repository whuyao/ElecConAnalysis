import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import math

###########1.数据生成部分##########

from sklearn.model_selection import train_test_split
data = pd.read_csv('E:\Geography and electricity\code\Regression\Test_0320_5.csv')
X = data[['road','小区',	'人口密度'	,'公司',	'交通',	'教育',	'金融'	,'购物'	,'医疗'	,'饮食',	'娱乐',
          '生活设施',	'旅馆'	,'light',	'坡度'	,'dis_road',	'dis_tielu',	'dis_huochezhan',	'dis_haiway']]
y = data[['SJSJ_2']]
x_train,x_test,y_train,y_test = train_test_split(X,y.values.ravel(),test_size=0.3)



###########2.回归部分##########
def try_different_method(model):
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    result = model.predict(x_test)
    print(len(result))
    for i in range(len(result)):
        sum_result=(y_test[i]-result[i])*(y_test[i]-result[i])
    mse_number=sum_result/len(result)
    print(mse_number)
    rmse_number=math.sqrt(mse_number)
    print(rmse_number)

    plt.figure()
    plt.plot(np.arange(len(result)), y_test,'go-',label='true value')
    plt.plot(np.arange(len(result)),result,'ro-',label='predict value')

    plt.title('score: %f'%score+' '+'rmse_number: %f'%rmse_number)

    plt.legend()
    plt.show()


###########3.具体方法选择##########
####3.1决策树回归####
from sklearn import tree
model_DecisionTreeRegressor = tree.DecisionTreeRegressor()
####3.2线性回归####
from sklearn import linear_model
model_LinearRegression = linear_model.LinearRegression()
####3.3SVM回归####
from sklearn import svm
model_SVR = svm.SVR(C=100,kernel='poly',degree=5)
####3.4KNN回归####
from sklearn import neighbors
model_KNeighborsRegressor = neighbors.KNeighborsRegressor()
####3.5随机森林回归####
from sklearn import ensemble
model_RandomForestRegressor = ensemble.RandomForestRegressor(n_estimators=100, max_features=10, max_depth=6, min_samples_leaf=8,
                oob_score=True)#这里使用20个决策树
####3.6Adaboost回归####
from sklearn import ensemble
model_AdaBoostRegressor = ensemble.AdaBoostRegressor(n_estimators=50)#这里使用50个决策树
####3.7GBRT回归####
from sklearn import ensemble
model_GradientBoostingRegressor = ensemble.GradientBoostingRegressor(n_estimators=100)#这里使用100个决策树
####3.8Bagging回归####
from sklearn.ensemble import BaggingRegressor
model_BaggingRegressor = BaggingRegressor()
####3.9ExtraTree极端随机树回归####
from sklearn.tree import ExtraTreeRegressor
model_ExtraTreeRegressor = ExtraTreeRegressor()

#model_DecisionTreeRegressor
#model_LinearRegression
#model_SVR
#model_KNeighborsRegressor
#model_RandomForestRegressor
#model_AdaBoostRegressor
#model_GradientBoostingRegressor
#model_BaggingRegressor
#model_ExtraTreeRegressor
###########4.具体方法调用部分##########
try_different_method(model_DecisionTreeRegressor)
try_different_method(model_LinearRegression)
try_different_method(model_SVR)
try_different_method(model_RandomForestRegressor)
try_different_method(model_ExtraTreeRegressor)