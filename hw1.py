# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:26:33 2022

@author: YAYA
"""
#************************************************************************
# Name: 楊雅涵
# Class: 資管系四年級
# SID: s08490069
 # Program Name: hw1.py
# Function: (1) input()
#(2) 操控 string 物件的方法
#(3) 第二章中所提到的各種運算子
#(4) If elif else
# Homework: No.1
# Limitations: (1). XXXXXXX
# Date: 2022/10/27
#************************************************************************



ID= input("請輸入輸入【身分證號碼】或【手機號碼】:")   #從鍵盤輸入號碼
print("************************************************************************")
print("*                                                                      *")
print("*                    HW1  程 式 輸 出 報 表                            *")
print("*                                                                      *")
print("************************************************************************")
if(ID[0].isalpha()):    #判斷第一個字元為英文就進入
    if(len(ID)==10):    #判斷字串長度為10就進入
        print("身分證號碼有效格式")  #在螢幕輸出
    else:  #若字串長度不為10就進入
        print("登入錯誤 – 無效格式")  #在螢幕輸出
elif(ID[0].isdecimal()):    #判斷第一個字元為數字就進入
    if(len(ID)==10):    #判斷字串長度為10就進入
        print("手機號碼有效格式")  #在螢幕輸出
    else:
        print("登入錯誤 – 無效格式")  #在螢幕輸出
else:
    print("登入錯誤 – 無效格式")  #在螢幕輸出
print("\n程式執行完畢時間2022-10-27 18:40:31")
print("楊雅涵 S08490069")
print("************************************************************************")
