from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
from matplotlib.offsetbox import AnchoredText

## 绘图
x1=[11.80552824,10.67541268,10.72086517,11.7466167,10.49541771,10.39626363,12.26613786,11.84866478,11.80218692,11.55207345,12.0223465]
y1=[17.69081983,15.98826756,16.18622148,16.99922749,16.22111242,15.8959516,17.03480629,16.58879904,16.68928902,16.42157971,16.83856613]
txt = ['南昌市','萍乡市','新余市','景德镇市','鹰潭市','九江市','上饶市','赣州市','吉安市','宜春市','抚州市']



fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
# ax1.plot(depths,training_scores,label="traing score")
x=np.arange(10,12.5,0.005)
y=0.624*x + 9.4858
plt.xlim(10,12.5)

plt.plot(x,y,'r',linestyle="--")

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

plt.annotate('南昌市', xy=(x1[0], y1[0]), xytext=(x1[0] + 0.05, y1[0]-0.05))  # 这里xy是需要标记
plt.annotate('萍乡市', xy=(x1[1], y1[1]), xytext=(x1[1] + 0.05, y1[1]-0.03))  # 这里xy是需要标记
plt.annotate('新余市', xy=(x1[2], y1[2]), xytext=(x1[2] + 0.05, y1[2]))  # 这里xy是需要标记
plt.annotate('景德镇市', xy=(x1[3], y1[3]), xytext=(x1[3] + 0.05, y1[3]))  # 这里xy是需要标记
plt.annotate('鹰潭市', xy=(x1[4], y1[4]), xytext=(x1[4] + 0.05, y1[4]))  # 这里xy是需要标记
plt.annotate('九江市', xy=(x1[5], y1[5]), xytext=(x1[5] + 0.05, y1[5]))  # 这里xy是需要标记
plt.annotate('上饶市', xy=(x1[6], y1[6]), xytext=(x1[6] + 0.05, y1[6]))  # 这里xy是需要标记
plt.annotate('赣州市', xy=(x1[7], y1[7]), xytext=(x1[7] + 0.05, y1[7]-0.02))  # 这里xy是需要标记
plt.annotate('吉安市', xy=(x1[8], y1[8]), xytext=(x1[8] + 0.05, y1[8]))  # 这里xy是需要标记
plt.annotate('宜春市', xy=(x1[9], y1[9]), xytext=(x1[9] + 0.05, y1[9]))  # 这里xy是需要标记
plt.annotate('抚州市', xy=(x1[10], y1[10]), xytext=(x1[10] + 0.05, y1[10]))  # 这里xy是需要标记

font1 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 12,
             }

at = AnchoredText('''$y = 0.624x + 9.4858$
$R^2 = 0.638$
$Pearson's$ $r = 0.799$
$p<0.01$''',
    prop=dict(size=14,family='Times New Roman'), frameon=True,
    loc='upper left'
    )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax1.add_artist(at)


#plt.text(4, 1, t, ha='right', rotation=15, wrap=True)


ax1.scatter(x1, y1,c = 'mediumblue',marker = 'o',edgecolors='k')




labels = ax1.get_xticklabels() + ax1.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

#plt.xticks(range(0,1050,50))               #设置x轴刻度

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
ax1.set_xlabel("ln(Jiangxi_elec)",font1)
ax1.set_ylabel("ln(GDP)", font1)
#ax1.legend(framealpha=0.5,prop={'family' : 'Times New Roman', 'size'   : 12})
plt.grid(True)
plt.show()

