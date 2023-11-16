
#3-5-2 もぐら
# def mogura(r):
#     m = ""
#     n = ""
#     for i in range(8):
#         ana = "."
#         if i==r:
#             ana = "O"
#         m = m + " _" + ana + "_ "
#         n = n + " [" + str(i) + "] "
#         print(m)
#         print(n)
        
# print("mogura関数を引数1で呼び出す")
# mogura(1)
# print("")
# print("mogura関数を引数5で呼び出す")
# mogura(5)


#3-5-3
import time
import random

def mogura(r):
    m = ""
    n = ""
    for i in range(8):
        ana = "."
        if i == r:
            ana = "O"
        m = m + " _" + ana + "_ "
        n = n + " [" + str(i) + "] "
    print(m)
    print(n)

print("-------------")
hit = 0
ts = time.time()
for i in range(10):
    r = random.randint(0,7)
    mogura(r)
    p = input("モグラはどこ？")
    if p == str(r):
        print("HIT!")
        hit = hit + 1
    else:
        print("MISS")
t = int(time.time()-ts)
bonus = 0
if t<60:
    bonus = 60-t
print("----------- ゲームエンド ---------")
print("TIME",t,"sec")
print("HIT",hit,"x BONUS", bonus)
print("SCORE",hit*bonus)







