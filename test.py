
#2-6-1
item = ["薬草","毒消し","たいまつ","短剣","木の盾"]
price = [10,20,40,200,120]

for i in range(5):
    print(item[i],"の値段は",price[i])

print()


#2-6-2
data = [[100,200,300,400,500],[-1,-2,-3,-4,-5],[55,66,77,88,99]]

print(data[0][0])
print(data[1][1])
print(data[2][4])

print()

#2-C-2
a=10
print(a,type(a))
b=10.0
print(b,type(b))
c=a+b
print(c,type(c))
s="Python"
print(s,type(s))
x=True
print(x,type(x))
y=False
print(y,type(y))

print()

"""
Pythonモジュール
random
time
tkinter
tkinter.messagebox
"""

#3-2-1
import random
for i in range(10):
    r = random.randint(1,6)
    print(r)

print()

"""
少数の乱数 0以上1未満
r = random.random()
整数の乱数 1から6のいずれかの整数
r = random.randint(1,6)
整数の乱数2 10以上20未満を2刻みに、10,12,14,16,18
r = random.randrange(10,20,2)
複数の項目からランダムに 7か8か9
r = random.choice([7,8,9])

"""

#3-C-1 おみくじ
KUJI =["大大吉","大吉","中吉","小吉","凶"]
input("おみくじを引きます([enterキー])")
print(random.choice(KUJI))

print()

#3-3-1
s = input("猫の英単語を入力してください")
if s == "cat":
    print("正解です")
else:
    print("猫はcatです")

print()

#3-3-2 

japanese = ["リンゴ","本","猫","犬","卵","魚","女の子"]
english = ["apple","book","cat","dog","egg","fish","girl"]
n = len(japanese)
for i in range(n):
    print(japanese[i]+"は"+english[i])

#3-3-3 英単語あて

right = 0
for i in range(n):
    a = input(japanese[i]+"の英単語は？")
    if a==english[i]:
        print("正解です")
    else:
        print("違います")
        print("正しくは"+english[i])
print("終了です")
print("正解数",right)
print("間違い",n-right)


#3-4-1 じゃんけん

hand = ["グー","チョキ","パー"]

for i in range(3):
    print("\n",i+1,"回目")
    c = random.randint(0,2)
    print("コンピュータの手は"+hand[c])

#3-4-2


print("コンピュータとじゃんけんをします")

for i in range(3):
    print("\n",i+1,"回目のじゃんけん")
    y = input("あなたは何を出す？ \n0=グー 1=チョキ 2=パー")
    y =int(y)
    c = random.randint(0,2)
    print("コンピュータの手は"+hand[c])
    if y==c:
        print("あいこです")
    if y==0:
        if c==1:
            print("あなたの勝ち")
        if c==2:
            print("コンピュータの勝ち")
    if y==1:
        if c==0:
            print("あなたの勝ち")
        if c==2:
            print("コンピュータの勝ち")
    if y==2:
        if c==0:
            print("あなたの勝ち")
        if c==1:
            print("コンピュータの勝ち")


#3-4-3 



hand = ["グー","チョキ","パー"]
you_win = 0
com_win = 0
print("コンピュータとじゃんけんをします")
print("3回じゃんけんをして勝敗を決めます")

for i in range(3):
    print("\n",i+1,"回目のじゃんけん")
    y=""
    while True:
        y = input("あなたは何を出す？ \n0=グー 1=チョキ 2=パー")
        if y=="0" or y=="1" or y=="2":
            break

    y = int(y)
    c = random.randint(0,2)

    print("コンピュータの手は"+hand[c])
    if y==c:
        print("あいこです")
    if y==0:
        if c==1:
            print("あなたの勝ち")
            you_win = you_win+1
        if c==2:
            print("コンピュータの勝ち")
            com_win = com_win+1
    if y==1:
        if c==0:
            print("あなたの勝ち")
            you_win = you_win+1
        if c==2:
            print("コンピュータの勝ち")
            com_win = com_win+1
    if y==2:
        if c==0:
            print("あなたの勝ち")
            you_win = you_win+1
        if c==1:
            print("コンピュータの勝ち")
            com_win = com_win+1

print("---------------------------------")
print("あなたが勝った回数",you_win)
print("コンピュータが勝った回数",com_win)
if you_win>com_win:
    print("あなたの勝利！")
elif com_win>you_win:
    print("コンピュータの勝利！")
else:
    print("引き分け")

print()

#3-5-1 タイム
import time
print("--------- 計測開始 ---------")
ts = time.time()
print("エポック秒",ts)
print("Enterキーを押すまでの時間を計測します")
te = time.time()
print("エポック秒",te)
print("---------- 計測終了 ---------")
print("経過秒数",int(te-ts))

print()

#3-5-2 もぐら
def mogura(r):
    m =""
    n =""
    for i in range(8):
        ana = "."
        if i==r:
            ana="0"
        m = m + " _" + ana + "_ "
        n = n + " [" + str(i) + "] "
        print(m)
        print(n)
        
print("mogura関数を引数1で呼び出す")
mogura(1)
print("")
print("mogura関数を引数5で呼び出す")
mogura(5)




