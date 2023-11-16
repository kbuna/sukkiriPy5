



#関数の応用テクニック


#5-18 2つの戻り値を返す？
def plus_and_minus(a,b):
    return a + b, a - b
next,prev = plus_and_minus(1978,1)

print(next)


# アンパック代入
# 変数をカンマで区切ってまとめて代入する
# カンマで区切られた＝タプル
# (a,b) = (1,2)  タプル同士の代入


#5-19 戻り値のタプルをアンパック代入
def plus_and_minus(a,b):
    return (a + b , a - b)
(next,prev) = plus_and_minus(1978,1)




"""
・デフォルト引数と引数のキーワード指定
end:などの設定されている引数

・デフォルト引数の制約
デフォルト引数の後にデフォルト引数がない引数を定義してはならない

・引数のキーワード指定
キーワード=""という風に指定した引数は、順序関係なく引き渡される

"""

#5-20 指定された3食を表示するeat関数
def eat(breakfast,lunch,dinner):
        
    print(f"朝は{breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"夕は{dinner}を食べました")

#5-21 松田くんの食生活を出力する
print("8月1日")
eat("トースト","おにぎり","カレー")
print("8月2日")
eat("納豆ごはん","ラーメン","カレー")
print("8月3日")
eat("バナナ","そば","焼肉")
print("8月4日")
eat("サンドウィッチ","しゅうまい弁当","カレー")

#5-22 指定された3食を表示するeat関数(デフォルト値を利用)
def eat(breakfast,lunch,dinner="カレー"):
    print(f"朝は{breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"夕は{dinner}を食べました")



#5-23 松田くんの言うまでもない食生活を出力する
print("8月1日")
eat("トースト","おにぎり")
print("8月2日")
eat("納豆ごはん","ラーメン")
print("8月3日")
eat("サンドウィッチ","しゅうまい弁当")

#5-24 松田くんの基本的なeat関数
def eat(breakfast,lunch="ラーメン",dinner="カレー"):
    print(f"朝は{breakfast}を食べました")
    print(f"昼は{lunch}を食べました")
    print(f"夕は{dinner}を食べました")

#5-25 夜がカレーじゃない日のeat関数の呼び出し
eat("納豆ごはん","ラーメン","カレーうどん")

#5-26 夜がカレーじゃない日のeat関数の呼び出し(キーワード指定)
eat(breakfast="納豆ごはん",dinner="カレーうどん")
eat(dinner="カレーうどん",breakfast="納豆ごはん")
eat("納豆ごはん",dinner="カレーうどん")




#5-27 おやつも出力できるeat関数
def eat(breakfast,lunch,dinner="カレー",desserts=()):
    print(f"朝は{breakfast}")
    print(f"昼は{lunch}")
    print(f"夕は{dinner}")
    for d in desserts:
        print(f"おやつに{d}を食べました")


#5-28 おやつも食べた日のeat関数の呼び出し
eat("トースト","パスタ","カレー",("アイス","チョコ","パフェ"))
##おやつの部分はタプルとして渡している


#5-29 おやつも出力できるeat関数(可変長引数を利用)
def eat(breakfast,lunch,dinner="カレー",*desserts):
    print(f"朝は{breakfast}")
    print(f"昼は{lunch}")
    print(f"晩は{dinner}")
    for d in desserts:
        print(f"おやつに{d}を食べました")

#5-30 おやつも食べた日のeat関数の呼び出し
eat("トースト","パスタ","カレー","アイス","チョコ","カレー")
#可変長引数
# 仮引数の前に *引数という風に書く
# 実引数をタプルで囲わずに書ける
# デフォルト引数のあとに可変長引数を持ってきてもいい

"""
ディクショナリを用いた可変長引数
def eat(**kwargs):
    for key in kwargs:
        print(f"{key}{kwargs[key]}")
eat(朝食="納豆",遅めの昼食="パスタ",夕方のおやつ="カレーパン")
"""





#5-31 引数を使わないで変数nameの値を受け渡している
name= "松田"
def hello():
    print("こんにちは"+name+"さん")
#5-32 hello関数の呼び出し
hello()
#5-33 グローバル変数に代入する
name ="松田"
def change_name():
    name = "浅木"
def hello():
    print("こんにちは"+name+"さん")

#5-34 関数の中からグローバル変数への代入を試みる
change_name()
hello()
#5-35 global文を用いてグローバル変数に代入する
name = "松田"
def change_name():
    global name
    name="浅木"

def hello():
    print("こんにちは"+name+"さん")

