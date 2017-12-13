import par as pa
import matplotlib.pyplot as plt
# import SQI_ECG_house as sqi
import numpy as np
from biosppy.signals import ecg as eecg
from biosppy.signals import tools as st
import time


# 原始code
filePath = 'zhuyan.CHE'
# filePath = 'D:\\LDC设备人体实带数据20171124\\LDC设备人体实带数据20171124\\李志光\C2\\00000015-2017_11_24-17_30_14.CHE'
cl = pa.ParseCHE(6)
data = cl.parse(filePath)

__respList__ = data['respList']
__respList__ = np.asarray(__respList__)
__respList__ = __respList__ - np.mean(__respList__)
__resp2List__ = data['resp2List']
__resp2List__ = np.asarray(__resp2List__)
__resp2List__ = __resp2List__ - np.mean(__resp2List__)

time_st = data['time']
x = data['xList']
y = data['yList']
z = data['zList']
spo2Val = data['spo2ValList']
###
####
aa = [time.localtime(x) for x in time_st]
timeArray = [time.strftime('%H:%M:%S', a) for a in aa]
timeArray = [timeArray[x1] for x1 in range(len(timeArray)) if (x1 % 2) == 0]

xindex_resp = list(range(len(__respList__)))
xindex_resp2 = list(range(len(__respList__)))
xindex_x = list(range(len(x)))
xindex_y = list(range(len(y)))
xindex_z = list(range(len(z)))
xindex_spo2Val = list(range(len(spo2Val)))
xindex_spo2Val = [int(xxx * 25) for xxx in xindex_spo2Val]


###
fig, ax = plt.subplots(3, sharex=True)
ax[0].plot(xindex_resp, __respList__, label='resp_Ch')
ax[0].plot(xindex_resp2, __resp2List__, label='resp_Ab')
ax[1].plot(xindex_spo2Val, spo2Val)
ax[2].plot(xindex_x, x)
ax[2].plot(xindex_y, y)
ax[2].plot(xindex_z, z)
ax[2].set_xticks(np.arange(0, len(xindex_x), 25*2))
ax[2].set_xticklabels(timeArray, rotation=80)
plt.show()


