
#3-5-2 もぐら
def mogura(r):
    m = ""
    n = ""
    for i in range(8):
        ana = "."
        if i==r:
            ana = "O"
        m = m + " _" + ana + "_ "
        n = n + " [" + str(i) + "] "
        print(m)
        print(n)
        
print("mogura関数を引数1で呼び出す")
mogura(1)
print("")
print("mogura関数を引数5で呼び出す")
mogura(5)


#3-5-3
