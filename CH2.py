# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:39:20 2022

@author: YAYA
"""
#第1題
print("第1題：")
year = int(input("請輸入你的出生年 : "))

a=year-1911
if a>90 :
    print("你是九年級生")
elif a<90 :
    print("你是八年級生")
else :
    print("你是2001年出生")
    
age = int(input("請輸入你的年齡: "))
b=year+age
if b>2022 :
    print("你算錯囉")
elif b<2022 :
    print("你程式錯了")
else :
    print("神奇吧把你的出生西元年加上你的年紀等於今年")
print("Over\n")

#第2題
print("第2題：")
score=int(input("輸入你想要的成績："))
time=int(input("輸入你學習的時間："))
a=score*0.3+time*0.7
print("你想要的成績：",score)
print("學習的時間：",time)
print("最終得分：",a)
if a<40 :
    print("請花更多時間學習\n")
elif 40.1<=a<=49.9 :
    print("加油你可以的\n")
elif 50.0<=a<=54.9 :
    print("快達到你想要的目標了\n")
else :
    print("好棒你達標了\n")

#第3題
print("第3題：")
a=input("輸入一個字元：")
if a.isalpha()==True:
  print(a,"is an alphabet.\n")
elif a.isdigit()==True:
  print(a,"is a number.\n")
else:
  print(a,"is a symbol.\n")

#第4題
print("第4題：")
a = eval(input("輸入一個正整數："))
ans=a%2
if(ans!=0):
  print(a,"is an odd number.\n")
else:
  print(a,"is not an odd number.\n")

#第5題
print("第5題：")
a=eval(input("第一個整數："))
b=eval(input("第二個整數："))
c=input("算術運算子：")
if(c=="+"):
  print(a+b-a,"\n")
elif(c=="-"):
  print(a*b-a,"\n")
elif(c=="*"):
  print(a*b*b,"\n")
elif(c=="/"):
  print(a-b/b,"\n")
  
#第6題
print("第6題：")
a=int(input("十進位："))
print(oct(a),hex(a),"\n")

#第7題
print("第7題：")
cost=int(input("請輸入購物金額，購物金額需大於12000（含）以上："))
if 12000<=cost<18000 :
    a=cost*0.8
    print("你的金額為：",cost,"打8折，打折過後金額為",a,"\n")
elif 18000<=cost<28000 :
    a=cost*0.7
    print("你的金額為：",cost,"打7折，打折過後金額為",a,"\n")
elif 28000<=cost<38000 :
    a=cost*0.6
    print("你的金額為：",cost,"打6折，打折過後金額為",a,"\n")
elif 38000<=cost :
    a=cost*0.5
    print("你的金額為：",cost,"打5折，打折過後金額為",a,"\n")

#第8題
print("第8題：")
score=int(input("輸入成績："))
if score%3==0 :
    a=score*10
    print("你的分數為：",score,"折扣後為",a,"\n")    
elif score%3==1 :
    a=score
    print("你的分數為：",score,"折扣後為",a,"\n")    
elif score%3==2 :
    a=score*1.1
    print("你的分數為：",score,"折扣後為",a,"\n")    


#第9題
print("第9題：")
word1="  *"
word2="***"
print(word1,"\n",word2,"\n")
#第10題
print("第10題：")
month=int(input("請輸入月份："))
if 2<=month<=4 :
    print("春\n")
elif 5<=month<=7 :
    print("夏\n")
elif 8<=month<=10 :
    print("秋\n")
else :
    print("冬\n")




