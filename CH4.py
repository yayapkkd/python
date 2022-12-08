#第1題
print("第1題")
nami,chop,null= 0,0,0

for i in range(5):
     vote = int(input())
     if vote == 1: nami +=1
     elif vote == 2: chop +=1
     else: null +=1
     
     print("Total vote of No.1: Nami =",nami)
     print("Total vote of No.2: Chopper =",chop)
     print("Total nul votes =" ,null)

if null >= nami and null >=chop or nami == chop: #先界定各種廢票
       print("=> No one won the election.")
elif nami> chop: 
       print("=> No.1 Nami won the election.")
else:
       print("=> No.2 Chopper won the election.")
       
       
#2題
print("第2題")
Y=0
while(Y!=-9999):
  Y=eval(input())
  if Y!=-9999:
    if Y%4==0 and Y%100!=0:
      print(Y,"is a leap year.")
    elif Y%400==0:
      print(Y,"is a leap year.")
    else:
      print(Y,"is not a leap year.")      
      
      
#第3題
print("第3題")     
n = eval(input('輸入一個正整數:'))

for  i  in range(0, n):
    for j in range( n-i,  1,  -1):
        print(' ', end=' ')
    for k in range( 0,  i * 2 + 1,  1):
        print('*', end=' ')
    print()      
    
    
#第4題
print("第4題")  
date=input("輸入年月日 ex:19110101 ：")
year,month,day=int(date[:4]),int(date[4:6]),int(date[6:])
month_set=[31,28,31,30,31,30,31,31,30,31,30,31]

if(year%400==0) or (year%400==0) and (year%100 !=0) and (month>2):
    d_sum=1
else:
    d_sum=0
i=0
for i in range(month-1):
    if i<(month-1):
        d_sum+=month_set[i]
        i+=1
d_sum+=day
print("%d年%d月%d日是這一年的第%d天"%(year,month,day,d_sum))

#第5題
print("第5題") 
s = 0
for i in range(1, 5):
   for j in range(1, 5):
       for k in range(1, 5):
            if i != j and i != k and j != k:
                print(i, j, k)
                s += 1
print("能生成的排列组合：", s)

#第6題
print("第6題") 
while 1:
    n = int(input('輸入一個整數：'))
    print('%d='%n,end='')
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                n=int(n/i)
                if n==1:
                    print('%d'%i,end='')
                    break
                else:
                    print('%d*'%i,end='')
                    break
                break
    print()

#第7題
print("第7題") 
x=100
sum=0
for i in range(10):
    x=x/2
    sum+=x*3
    print("第{}次彈跳反彈{}米。一共經過{}米。".format(i+1,x,sum-x))

#第8題
print("第8題") 
import random
print("----石頭剪刀布遊戲開始----")
print("請按下面提示出拳")
print("石頭[1],剪刀[2],布[3],退出[4]")
while True:
    user = int(input("請玩家出拳："))
    computer=random.randint(1,3)
    if user==4:
        print("遊戲退出")
        break
    if ((computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2)):
        print("玩家出拳為{}，電腦出拳為{}，玩家勝利".format(user, computer))
    elif computer == user:
        print("玩家出拳為{}，電腦出拳為{}，平局".format(user, computer))
    else:
        print("玩家出拳為{}，電腦出拳為{}，電腦勝利".format(user, computer))
print("遊戲結束")

#第9題
print("第9題") 
import random
import operator
def auto():
    pokers=[]
    poker=[]
    for i in ['♥','♠','♦','♣']:
        for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            poker.append(i)
            poker.append(j)
            pokers.append(poker)
            poker=[]
    return pokers
poker=auto()
random.shuffle(poker)
li={}
for k in ['player1','player2','player3','player4']:
    b=random.sample(poker,13)    
    for s in b:
        poker.remove(s)
    li.setdefault(k,b)        
print(sorted(li['player1'],key=operator.itemgetter(0,1)))
print(sorted(li['player2'],key=operator.itemgetter(0,1)))   
print(sorted(li['player3'],key=operator.itemgetter(0,1)))
print(sorted(li['player4'],key=operator.itemgetter(0,1)))

#第10題
print("第10題")
TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print ('平方運算後小於50則退出')
again = 1
while again:
    num = input('輸入一個數字：')
    
    if num.isdigit():
        num=int(num)
        print ('其平方為: %d' % (SQ(num)))
        if SQ(num) >= 50:
            again = TRUE
        else:
            again = FALSE
    else:
        print("輸入錯誤")









