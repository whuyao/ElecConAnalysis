from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import math
from scipy import stats

data = pd.read_csv('test_data\\test_train_data.csv')
pd.set_option('display.max_columns', None)
X = data[['dis_trainstation','dis_road','dis_river','dis_railway','transportation','slope','Shopping','restaurant','population','nightlight','hotel','hospital','finance','entertainment','enterprise','elevation','education','dailyfacility','community']]
y = data[['SJSJ']]
X_train,X_test,y_train,y_test = train_test_split(X,y.values.ravel())

def getRMES(pred, test):
    for i in range(len(pred)):
        sum_result = (test[i] - pred[i]) * (test[i] - pred[i])
    mse_number = sum_result / len(pred)
    return math.sqrt(mse_number)


#随机森林模型
clf = RandomForestRegressor(n_estimators=500)

#支持向量机模型
#clf = SVR(kernel='rbf', C=10, gamma=0.1)

#人工神经网络模型
#clf = MLPRegressor(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(6,6,6,6,6), random_state=2)

#线性回归模型
#clf = linear_model.LinearRegression()

clf = clf.fit(X_train,y_train)
print(clf.estimators_[5])
print("RMSE: ", getRMES(clf.predict(X_test), y_test))
print("R2: ", clf.score(X_test, y_test))
print("权重：", clf.feature_importances)
print("Pearson R: " , stats.pearsonr(y_test, clf.predict(X_test)))