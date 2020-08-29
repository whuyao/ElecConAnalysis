from osgeo import gdal
import struct
import numpy
from sklearn.externals import joblib

#打开栅格数据文件
dataset = gdal.Open("G:\测试\part1.tif",gdal.GA_ReadOnly)

#获取数据集信息
print("Driver: {}/{}".format(dataset.GetDriver().ShortName,dataset.GetDriver().LongName))
print("Size is {} x {} x {}".format(dataset.RasterXSize,dataset.RasterYSize,dataset.RasterCount))
geotransform = dataset.GetGeoTransform()
if geotransform:
    print("Origin = ({}, {})".format(geotransform[0], geotransform[3]))
    print("Pixel Size = ({}, {})".format(geotransform[1], geotransform[5]))

#波段数设置
bandcount = 19;



fileformat = "GTiff"
driver = gdal.GetDriverByName(fileformat)
metadata = driver.GetMetadata()
if metadata.get(gdal.DCAP_CREATE) == "YES":
    print("Driver {} 支持Create（）方法。".format(fileformat))

if metadata.get(gdal.DCAP_CREATE) == "YES":
    print("Driver {} 支持CreateCopy（）方法。".format(fileformat))

cols = dataset.RasterXSize
rows = dataset.RasterYSize
outDataset = driver.Create("D:\Result\\finalTif\InitialRes_15.tif", cols, rows, 1, gdal.GDT_Float32)

#同步基准面与坐标
geoTransform = dataset.GetGeoTransform()
outDataset.SetGeoTransform(geoTransform )
proj = dataset.GetProjection()
outDataset.SetProjection(proj)

#加载随机森林模型
RF=joblib.load('D:\Result\CSVDATA\\train_model.m')

#跑随机森林回归模型
def runModel(X):
    out = RF.predict(X);
    return out

#输出栅格波段
outBand = outDataset.GetRasterBand(1)
ND = dataset.GetRasterBand(1).GetNoDataValue()
outBand.SetNoDataValue(ND)

xBlockSize = 100
yBlockSize = 100
for i in range(0, rows, yBlockSize):
   if i + yBlockSize < rows:
        numRows = yBlockSize
   else:
        numRows = rows - i
   for j in range(0, cols, xBlockSize):
        if j + xBlockSize < cols:
             numCols = xBlockSize
        else:
             numCols = cols - j
        data = []
        for k in range(1,bandcount+1):
            data.append(dataset.GetRasterBand(k).ReadAsArray(j, i, numCols, numRows).astype(numpy.float32))

        # do calculations here to create outData array
        outData = numpy.zeros((numRows, numCols), numpy.float32)
        for n in range(0,numRows):
            for m in range(0,numCols):
                Temp = []
                X_pred =[]
                if data[0][n,m] != ND:
                    for k in range(0,bandcount):
                        Temp.append(data[k][n,m])
                    X_pred.append(Temp)
                    outD = runModel(X_pred)[0].astype(numpy.float32)
                    outData[n,m] = outD
                    print("第" + i.__str__() + "行"+j.__str__() + "列块"+"                   第 " + n.__str__() + " / 100 行  " + m.__str__() + " / 100 列");
                else :
                    outData[n, m] = data[0][n,m];
        outBand.WriteArray(outData, j, i)
