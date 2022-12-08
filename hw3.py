# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:26:33 2022

@author: YAYA
"""
#************************************************************************
# Name: 楊雅涵
# Class: 資管系四年級
# SID: s08490069
 # Program Name: hw3.py
# Function: (1) input()
#(2) re
#(3) 運算子
#(4) If elif else
#(5) for 迴圈
#(6) 字典 Dictionary
#(7) time
# Homework: No.3
# Limitations: (1). XXXXXXX
# Date: 2022/10/27
#************************************************************************



print("************************************************************************")
print("*                                                                      *")
print("*                    HW3  程 式 輸 出 報 表                            *")
print("*                                                                      *")
print("************************************************************************")
import re    # 引入re模組，用來將標點符號去除
import time  # 引入time模組，用來顯示程式結束時會自動取得當地的日期時間
MORSECODE = {
                   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..', 
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
                   '7': '--...', '8': '---..', '9': '----.', '0': '-----', 
                   ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
                   '(': '-.--.', ')': '-.--.-'
                   } #創建字典
def encrypt(sentence): # 將字符串從英文的函數解密為摩斯密碼
    cipher = ''
    for a in sentence:
        if a != ' ':
            # 查字典並添加對應的摩斯密碼
            # 用空格分隔不同字符的摩斯密碼
            cipher += MORSECODE[a] + ' '
        else:
            # 1個空格表示不同的字符
            # 2表示不同的詞
            cipher += ' '
    return cipher

def decrypt(sentence):# 將字符串從摩斯密碼解密為英文的函數
    # 在末尾添加額外空間以訪問最後一個摩斯密碼
    sentence += ' '
    decipher = ''
    citext = ''
    global i
    for a in sentence:# 檢查空間
        if a != ' ':
            i = 0# 在空格的情况下
            citext += a# 在空間的情况下
        else:
            # 如果 i = 1 表示一個新字符
            i += 1
            # 如果 i = 2 表示一個新單詞
            if i == 2:
                # 添加空格來分隔單詞
                decipher += ' '
            else:
                # 使用它們的值訪問密鑰（加密的反向）
                decipher += list(MORSECODE.keys())[list(MORSECODE.values()).index(citext)]
                citext = ''
    return decipher
sentence = input("請輸入一行英文句子？") #輸入單詞
out = re.sub(r'[^\w\s]','',sentence)   #將輸入的標點符號刪除
result = encrypt(out.upper())         #將字符串中的小寫字母轉為大寫字母並加密

print("\n",sentence,"的摩斯密碼為 =>",result) #輸出摩斯密碼
print ("\n本機時間為 : ",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"執行完畢")# 輸出時間
print("楊雅涵 S08490069")
print("************************************************************************")
