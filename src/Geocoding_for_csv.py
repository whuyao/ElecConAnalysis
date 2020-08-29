import os
import json
import requests
import csv
import pandas 
import string
import math
import time
import xlrd
import xlwt
from xlwt import Workbook
from xlutils.copy import copy

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方

def geocodeB(address,wait_handle):
    address1=address[0]
    lng_lat=[]
    base1 = url = "http://api.map.baidu.com/geocoder?address=" + address1 + "百度apikey"
    response1 = requests.get(base1)

    answer1 = response1.json()

    if answer1['result']==[]:
        address2=address[1]
        base2 = url = "http://api.map.baidu.com/geocoder?address=" + address2 + "百度apikey"
        response2 = requests.get(base2)

        answer2 = response2.json()      
        if answer2['result']==[]:           
            handle_null_data(wait_handle)
            lng_lat.append(wait_handle)
            lng_lat.append(0)
            lng_lat.append(0)
            lng_lat.append(0)
            
        else:
            address2=address[1]
            lng=answer2['result']['location']['lng']
            lat=answer2['result']['location']['lat']
            level=answer2['result']['level']
            final=(bd09_to_wgs84(lng, lat))
    
            lng_lat.append(address2)
            lng_lat.append(final[0])
            lng_lat.append(final[1])
            lng_lat.append(level)
            response2.close()
            
    else:
        lng=answer1['result']['location']['lng']
        lat=answer1['result']['location']['lat']
        level=answer1['result']['level']
        final=(bd09_to_wgs84(lng, lat))
    
        lng_lat.append(address1)
        lng_lat.append(final[0])
        lng_lat.append(final[1])
        lng_lat.append(level)
        
    response1.close()

    time.sleep(0.05)
       
    return(lng_lat)

def read_by_room(name):
    print(name+'开始处理')
    location=[]
    with open(name, "r", encoding="utf-8") as csvfile:
       reader = csv.reader(csvfile)
       data = [row for row in reader]
       data_rows=len(data)-1
    for row in range(data_rows):
        print(row)
        wait_handle=data[row+1]
        handlded=get_address(wait_handle)        
        final=geocodeB(handlded,wait_handle)
        final.append(str(wait_handle[2]))
        final.append(str(wait_handle[3]))
        location.append(final)

    return location


def get_address(data):
    city=data[0]
    county=data[1]
    town=data[4]
    road=data[5]
    machine=data[6]
    ad=[]

    city_handle(city)
    county_handle(county)
    town_handle(town)
    #road_handle(road)
    #machine_handle(machine)
    
    address1=city_handle(city)+' '+county_handle(county)+' '+town_handle(town)+' '+machine_handle(machine)
    address2='江西'+' '+town_handle(town)+' '+machine_handle(machine)
    
    return address1,address2

    
    
def city_handle(c):
    i=c.translate(str.maketrans('','','国网'))
    t=i.translate(str.maketrans('','','供电公司'))
    return t
    
def county_handle(c):
    o=c.translate(str.maketrans('','','国网'))
    u=o.translate(str.maketrans('','','供电分公司'))
    return u
    
def town_handle(t):
    t=list(filter(lambda ch: ch not in ' \t1234567890', t))
    t=''.join(t)
    o=t.translate(str.maketrans('','','kV'))
    w=o.translate(str.maketrans('','','变电站'))
    return w

    
def road_handle(r):
    r=list(filter(lambda ch: ch not in ' \t1234567890', r))
    r=''.join(r)
    o=r.translate(str.maketrans('','','kV'))
    a=o.translate(str.maketrans('','','开关间隔'))
    return a
    
def machine_handle(m):
    m=list(filter(lambda ch: ch not in ' \t1234567890', m))
    m=''.join(m)
    a=m.translate(str.maketrans('','','kV'))
    c=a.translate(str.maketrans('','','公变'))
    h=c.translate(str.maketrans('','','箱变'))
    i=h.translate(str.maketrans('','','室变'))
    n=i.translate(str.maketrans('','','变'))
    l=n.translate(str.maketrans('','','号'))
    s=l.translate(str.maketrans('','','#'))
    t=s.translate(str.maketrans('','','电网_'))
    
    return t
    

def write_by_room(fils_name,address):
    os.chdir('E:\产学研\data_handling_for_csv\handling_data')
    filename=fils_name.split('.')[0]
    name=filename+'处理结果.csv'
    out = open(name,'a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    for ad in range(len(address)):
        csv_write.writerow(address[ad])
    print(filename+'处理完成')

def handle_null_data(wait_handle):
    row=1
    os.chdir('E:\产学研\data_handling_for_csv\handling_data')
    name='异常数据.xls'
    filename = name
    workbook = xlrd.open_workbook(filename, formatting_info=True)
    sheet = workbook.sheet_by_index(0)
    rowNum = sheet.nrows
    colNum = sheet.ncols
    newbook = copy(workbook)
    newsheet = newbook.get_sheet(0)
    # 在末尾增加新行
    str = wait_handle
    newsheet.write(rowNum, 0, str)
    # 覆盖保存
    newbook.save(filename) 

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.csv':  
                L.append(os.path.join(file))  
    return L    

def bd09_to_gcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]

def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]
    
def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret
 
 
def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret



def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)

if __name__ == '__main__':
    time_start=time.time()
    file_dir=os.getcwd()                                                 #获取文件夹位置
    fils_name=file_name(file_dir)                                        #获取指定文件夹中的所有文件名
    
    for num in range(len(fils_name)):
        os.chdir('E:\产学研\data_handling_for_csv\data')
        file_name=fils_name[num]                                         #file_name 文件名

        
        AD=read_by_room(file_name)

        write_by_room(file_name,AD)
        
    time_end=time.time()
    print('totally cost',time_end-time_start)
        
