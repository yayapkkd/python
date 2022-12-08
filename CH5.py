# In[] 第1題
print("第1題")
def com(i):
    if i<=1:
        return i
    else:
        return com(i-1)+com(i-2)
 
num=eval(input("輸入一正整數num (num>=2)："))
for i in range(num):
    print(com(i),end=" ")
print()
# In[] 第2題
print("第2題")
print('判斷傳入物件的長度是否大於5')
def fun1(n):
    if len(n) >= 5:
        return True
    else:
        return False
content = input('請輸入內容:')
print(fun1(content))
# In[] 第3題
print("第3題")
def X(*a):    
    for i in range(len(a)):
        print(a[i])
X('1','2','3','Hi','5','Hi','7')
# In[] 第4題
print("第4題")
def x(str1):
    y=''
    for i in str1:
        if i.isalpha():
            y+=i
    return y
result=x(input())
print(result)
# In[] 第5題
print("第5題")
prompt = "\nPlease enter the your age:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True :
  age = input(prompt)
  if age == 'quit':
    break
  else:
      age=int(age)
      if age<3:
          print("free")
      elif (age>=3 and age<=12):
          print("The ticket price is 10 dollars.")
      else:
          print("The ticket price is 15 dollars.")
# In[] 第6題
print("第6題")          
def add(n,m):
    n=n+m
    return n
num=int(input("請輸入一個值："))
num1=int(input("請輸入一個值："))
num2=add(num,num1)
print(num2)
# In[] 第7題
print("第7題")
import re
def stat(s):
    letter="[a-zA-z]"
    digital="[0-9]"
    blank="[ ]"
    letter_num=0
    digital_num=0
    blank_num=0
    for i in s:
        if(re.match(letter, i))!=None:
            letter_num+=1
        if(re.match(digital, i))!=None:
            digital_num+=1
        if(re.match(blank, i))!=None:
            blank_num+=1
    others=len(s)-letter_num-digital_num-blank_num
    return letter_num,digital_num,blank_num,others
if __name__=="__main__":
    s=input("輸入字串")
    print("字母的數量："+str(stat(s)[0]))
    print("數字的數量："+str(stat(s)[1]))
    print("空格的數量："+str(stat(s)[2]))
    print("符號的數量："+str(stat(s)[3]))
# In[] 第8題
print("第8題")
print("有一個程式如下，其輸出結果為20 20，請說明輸出之結果為何不是回傳20 30")
print("num = 20\ndef show_num(x=num):\nprint(x)\nshow_num()\nnum = 30\nshow_num()")
print("因為上面的num是全域變數，只要在同一個Python檔案中，皆可進行存取；而下面的num是區域變數，只有在函式的範圍中都可以進行存取，而函式以外的其它地方，則無法進行存取")
# In[] 第9題
print("第9題")
def a(n):                   
    if n == 0 or n == 1:     
        return 1             
    else:
        return n * a(n-1)    
num=int(input("輸入一個值，計算階層："))
print(a(num))                  
# In[] 第10題
print("第10題")
def demo():
    result = []
    for i in range(1, 1000):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            result.append(str(i))
    return ",".join(result)

print("1000以内的完全數有：{}".format(demo()))















