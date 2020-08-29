import pandas as pd


data1_file="Geo_GaodeResult.csv"             #新数据
data2_file="Geo_BYQJH.csv"                 #老数据

data_old=pd.read_csv(data2_file)
data_new=pd.read_csv(data1_file)

print(data_old.head())
print(data_new.head())

load_left=pd.merge(data_old,data_new,how='left',left_on='BYQJH',right_on='BYQJH')
print(load_left.head())



load_left.to_csv("result.csv")
