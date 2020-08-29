import pandas as pd
import numpy as np
import math
import os

def handle_xls(name):  # 打开对应文件
    handle_data = []
    data_df = pd.read_excel(name)
    data_list = data_df.values.tolist()
    final_data = []
    global ID_df

    for n in range(len(data_list)):
        if data_list[n][7] > 0:
            data_list[n][7] = math.log(float(data_list[n][7]), math.e)
            handle_data.append(data_list[n][7])
        elif data_list[n][7] < 0:
            data_list[n][7] = 0

    data_mean = np.mean(handle_data)
    print(data_mean)
    data_std = np.std(handle_data, ddof=0)
    print(data_std)
    data_top = data_mean + 3 * data_std  # 计算标准差 平均值
    data_low = data_mean - 3 * data_std

    for n in range(len(data_list)):
        if data_list[n][7] != 0:
            if data_list[n][7] >= data_top:
                data_list[n][7] = data_top

    for n in range(len(data_list)):
        if data_list[n][7] != 0:
            if data_list[n][7] <= data_low:
                data_list[n][7] = data_low

    for n in range(len(data_list)):
        if data_list[n][7] != 0:
            data_list[n][7] = (data_list[n][7] - data_low) / (data_top - data_low)
            if data_list[n][7] == 0:
                print('ok')

    for n in range(len(data_list)):
        final_data.append([])
        final_data[-1].append(data_list[n][1])
        final_data[-1].append(data_list[n][7])

    pp.append([])

    name_str = name.split('.')[0]

    pp[-1].append(name_str)
    pp[-1].append(data_top)
    pp[-1].append(data_low)
    pp[-1].append(data_mean)
    pp[-1].append(data_std)

    test_name = ['OBJECTID_1', name_str]
    test = pd.DataFrame(columns=test_name, data=final_data)
    ID_df = pd.merge(ID_df, test, how='left', left_on='OBJECTID_1', right_on='OBJECTID_1')

def get_filename():
    file_dir = os.getcwd()  # 获取文件夹位置
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xls':
                L.append(os.path.join(file))
    return L  # 获取指定文件夹中的所有文件名


if __name__ == '__main__':

    filenames = get_filename()
    pp = []

    ID_df = pd.read_excel("ID.xlsx")
    print(ID_df.head())

    for name in filenames:
        print(name)
        handle_xls(name)
    pp_name = ['feature', 'data_top', 'data_low', 'data_mean', 'data_std']
    pp_test = pd.DataFrame(columns=pp_name, data=pp)
    pp_test.to_csv("参数.csv", index=None)

    ID_df.to_csv("汇总表格.csv", index=None)
