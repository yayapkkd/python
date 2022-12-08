#
# 請將您完成本次作業所需要的程式碼直接寫在本檔案內
#
#************************************************************************
# Name: 楊雅涵
# Class: 資管系四年級
# SID: s08490069
 # Program Name: hw4.py
# Function: 
#(1) 運算子
#(2) If elif else
#(3) for 迴圈
#(4) 字典 Dictionary
#(5) count()
#(6) list()
#(7) len()
# Homework: No.4
# Date: 2022/12/1
#************************************************************************



print("************************************************************************")
print("*                       S08490069 楊雅涵                               *")
print("*                    HW4  程 式 輸 出 報 表                            *")
print("*                                                                      *")
print("************************************************************************")
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""    #定義了一個字符串變量


d = {}      #定義了一個空的字典類型的變量

#
# 說明：以下為 ASCII 碼對應字元的解密置換表。
#       您必須完全看懂以下的程式意涵，才能
#       逆向反推如何再加密回來！
#
# In[] a解密
for c in (65, 97):      #在ASCII碼中，65對應大寫字母A，97對應小寫字母a，（65，97）是元組類型，該句循環在元組中遍歷，執行循環體中的代碼
    
    for i in range(26):     #range返回一個列表[0,1,2,..,25]，26是因為有26個字母
        
        d[chr(i+c)] = chr((i+13) % 26 + c)      #第一個循環遍歷到第一個元素，c=65，第二個循環i=0，於是i+c=65，chr(i+c)是強制類型轉換，轉為字符型，即chr(65)變成A，等號右邊同理，變成第13個字母M。第二個循環遍歷後，就完成了大寫字母的加密對應關係。
print(">> (a)小題 : 顯示解密的原文內容")           #輸出a小題
print("".join([d.get(c, c) for c in s]))        #從字典d中找到c對應的值並返回，如果沒有查找到對應的鍵值對則返回c本身，由此可見它的作用就是遇到單詞之間的空格時返回空格本身，不至於在字典中查找不到而出現ERROR。
print()
# In[] b再加密並比對
print(">> (b)小題 : 比對'再加密之後的字串'與'解密前的字串'內容是否相同無誤")           #輸出b小題
L=len(s)	#求字串長度
b=list(s)   #將字串變成串列
for i in range(L): #一個字一個字去加密
  if 97<=ord(b[i])<=122: #小寫加密，ord()就是把字母改寫成ASCII碼的函數
    b[i]=(chr((ord(s[i]))))
  elif ord(s[i])<97: 
    pass
  else:
    b[i]=(chr((ord(b[i])+5)-26)) #大寫加密，ord()就是把字母改寫成ASCII碼的函數
b=''.join(b)        #找到對應的值並返回

if s == b:          #比對s和b的值是否相同
    print("比對結果 :加密內容經比對後正確無誤！")           #若相同輸出正確
else:
    print("比對結果 :您的程式有誤，請務必修正。")           #若不相同輸出錯誤
# In[] c字元個數
print(">> (c)小題 : 計算並顯示執行(a)解密之後原文中的字元個數(包含標點符號與空白)")
la=[d.get(c, c) for c in s]
print("原文解密後的字元個數 ：",len(la)) #輸出字元個數
# In[] d文字處理
print(">> (d)小題 : 將(a)解密之後的原文做(1)字元分類與(2)計算相同字元出現的次數")
print("字元分類與出現個數 ：")
print("字元:出現次數")
print("=============")
print("'\\n':",la.count('\n')) #輸出指定字元的個數
print("' ' :",la.count(' '))    
print("'!' :",la.count('!'))
print("''' :",la.count("'"))
print("'*' :",la.count("*"))
print("',' :",la.count(","))
print("'-' :",la.count("-"))
print("'.' :",la.count("."))
print("'A' :",la.count("A"))
print("'B' :",la.count("B"))
print("'C' :",la.count("C"))
print("'D' :",la.count("D"))
print("'E' :",la.count("E"))
print("'F' :",la.count("F"))
print("'I' :",la.count("I"))
print("'N' :",la.count("N"))
print("'P' :",la.count("P"))
print("'R' :",la.count("R"))
print("'S' :",la.count("S"))
print("'T' :",la.count("T"))
print("'U' :",la.count("U"))
print("'Z' :",la.count("Z"))
print("'a' :",la.count("a"))
print("'b' :",la.count("b"))
print("'c' :",la.count("c"))
print("'d' :",la.count("d"))
print("'e' :",la.count("e"))
print("'f' :",la.count("f"))
print("'g' :",la.count("g"))
print("'h' :",la.count("h"))
print("'i' :",la.count("i"))
print("'k' :",la.count("k"))
print("'l' :",la.count("l"))
print("'m' :",la.count("m"))
print("'n' :",la.count("n"))
print("'o' :",la.count("o"))
print("'p' :",la.count("p"))
print("'r' :",la.count("r"))
print("'s' :",la.count("s"))
print("'t' :",la.count("t"))
print("'u' :",la.count("u"))
print("'v' :",la.count("v"))
print("'w' :",la.count("w"))
print("'x' :",la.count("x"))
print("'y' :",la.count("y"))

print("\nPress enter key to exit...")



