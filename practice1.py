# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:18:35 2022

@author: admin
"""

'''  Paper Bag Defect Verification  '''


import os
import cv2
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#path0 = input('請輸入此資料夾路徑: ')  
path0 = 'C:/Users/admin/Desktop/project'
#路徑中不要包含中文字元，不然imread()會返回Nonetype，讀取不到圖片!!

path1 = path0 + '/test/'

jpgs = [f for f in os.listdir(path1) if f.endswith('.jpg')]  
#os.listdir為會讀取指定路徑中的所有檔案，再用if篩選出要使用的jpg檔案
#endswith用以判斷檔案名稱的結尾，也就是副檔名的部分

jpgs = sorted(jpgs)
'''
sorted() --> 對所有可迭代的對象進行排序  
EX:sorted(iterable, cmp=None, key=None, reverse=False)
interable:迭代對象(此處為jpg(type = list))

'''

file = [f for f in jpgs if 'file' in f]  # 所有良品檔名

######檢視照片長寬
df = pd.DataFrame({'img_h': [-1], 'img_w': [-1]}, index = jpgs)
# 創建一個DataFrame名為df以記錄圖片長寬。其中包含兩個欄位
#img_h:紀錄圖片長度
#img_w:紀錄圖片寬度

path2 = path0 + '/output/'

os.chdir(path2)#更改當前位置至指定路徑path2

for i in range(int(len(df))):
    img = cv2.imread(path1 + df.index[i])    
    df['img_h'][i] = len(img[1])  # 長
    df['img_w'][i] = len(img[0])  # 寬
try: 
    os.mkdir('resize')  # 創建一資料夾resize用以後續存放統一長寬後的圖片
except: 
    pass


###########加上白色邊框統一照片長寬(去除輸送帶)
for i in range(len(df)):
    blank = np.ones((550,700,3), np.uint8)  # 生成空畫布 (黑)
    '''
    numpy.ones() --> 設定一特定形狀和類型的陣列
    numpy.ones(shape, dtype=None, order='C', *, like=None)
    shape： 整數或整數序列
    dtype： 數據類型，可選(uint8 = 8 位無符號整數)
    '''
    blank *= 255  # 畫布轉為白色
    img = cv2.imread(path1 + df.index[i])
    h, w, c = img.shape    # 手工繪製ROI區域  
    mask = np.zeros((h, w), dtype=np.uint8)  #設定掩膜
    x_data = np.array([63,52,581,635])  #設定掩膜x軸點座標
    y_data = np.array([1,395,431,0])  #設定掩膜y軸點座標
    pts = np.vstack((x_data, y_data)).astype(np.int32).T #使用vstack將x_data和y_data垂直排列  https://vimsky.com/zh-tw/examples/usage/python-numpy.vstack.html
    cv2.fillPoly(mask, [pts], (255), 4, 0) #使用fillpoly 對上述頂點進填充   https://blog.csdn.net/lyxleft/article/details/90676451
    img = cv2.bitwise_and(img, img, mask=mask) #透過bitwise_and進行二進制and的運算，保留掩膜白色部分(切割出的圖形)，去除黑色部分   https://www.796t.com/content/1544893570.html
    a = int(round((len(blank) - len(img))/2, 0))
    c = a + len(img) 
    b = int(round((len(blank[0]) - len(img[0]))/2, 0))
    d = b + len(img[0])
    blank[a:c, b:d] = img  # 照片置中覆蓋
    cv2.imwrite('./resize/' + jpgs[i], blank)
    '''
    imwrite() --> 依據指定的格式將圖片存至指定路徑中
    '''

# 建立output資料夾
folders = ['title', 'threshold_title', 'threshold2', 'threshold3', 'results','threshold_mark','resize','mark']
lst = glob.glob('./*')
for i in folders:
    if i not in lst:
        try: os.mkdir(i)
        except: pass
        
# In[ DETECT-1: compute black directly (title) ]

    
def contrast(img, a = 1.7):  # 對比度調整
    O = img * float(a)
    O[O > 255] = 255
    O = np.round(O)  # 四捨五入
    O = O.astype(np.uint8)
    return O


def PreProcess(img, i): #對照片做前置處理
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # RGB轉灰階
    cont = contrast(gray)  # 對比度增加
    blur = cv2.GaussianBlur(cont, (5,5), 0)  # 高斯模糊降噪 
    '''
    (5,5)高斯核尺寸  0:標準差 -->核尺寸、標準差越高，圖片越模糊
    https://www.gushiciku.cn/pl/gWtk/zh-tw
    '''
    return blur

#圖片前置處理       
for i in range(len(df)): 
    img = cv2.imread('./resize/' + df.index[i])
    blur = PreProcess(img, df.index[i])
    thresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)[1]  # 二值化
    cv2.imwrite('./threshold_title/' + df.index[i].replace('.', 'thresh_title.'), thresh)    
    '''
    https://shengyu7697.github.io/python-opencv-threshold/
    '''
#計算標題面積
area_title = []
for i in range(len(df)):
    count = 0
    img = cv2.imread(path2+'./title/' + jpgs[i].replace('.', 'title.'),cv2.IMREAD_COLOR)
    x,y,chenels = np.shape(img)
    for a in range(x):
        for b in range(y):
            if img[a,b].all() == 0: #rgb ==0 代表黑色，此處是判斷像素是否為黑色
                count+= 1
    area_title.append(count)
print("area_title\n",area_title)
print("Max:",max(area_title))
print("Min:",min(area_title))