
#関数の基本的な使い方 引数ありなし/戻り値ありなし
def hello():
    print("hello everyone!")

def add(a,b):
    return a+b

hello()
result = add(5,10)
print(result)




#5-1 見通しの悪いプログラム
student_list = ["浅木","松田"]
for student in student_list:
    print(f"{student}さんの試験結果を入力してください")
    network = int(input("ネットワークの点数？ >>"))
    database = int(input("データベースの点数？ >>"))
    security = int(input("セキュリティの点数？ >>"))
    if student == "浅木":
        asagi_scores = [network,database,security]
        asagi_avg = sum(asagi_scores)/len(asagi_scores)
    else:
        matsuda_scores = [network,database,security]
        matsuda_avg = sum(matsuda_scores)/len(matsuda_scores)
print(f"浅木さんの平均点は{asagi_avg}")
print(f"松田さんの平均点は{matsuda_avg}")


# 5-2

#例題が動作するように関数を実装
def input_scores(name):
    scores =[]
    scores.append(int(input(f"{name}さんのネットワーク点数入力")))
    scores.append(int(input(f"{name}さんのデータベース点数入力")))
    scores.append(int(input(f"{name}さんのセキュリティ点数入力")))
    return scores

def calc_average(scores):
    total = sum(scores)
    return total / len(scores)

def output_result(name, avg):
    print(f"{name}さんの平均点は{avg}")
    pass

#得点を入力
asagi_scores = input_scores("浅木")
matsuda_scores = input_scores("松田")
#結果を入力
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)
#結果を出力
output_result("浅木",asagi_avg)
output_result("松田",matsuda_avg)



# 5-3 hello関数の定義

def hello():
    print("こんにちは。工藤です。")

# 5-4 hello関数の呼び出し
hello()

#シンプルな関数の定義
# def 関数名()
#     処理

#シンプルな関数の呼び出し
# 関数名()

# 5-5　名前を表示するつもりのinput_scores関数
def input_scores():
    name= ""
    print(f"{name}")

# 5-6 input_socores関数内の変数nameに代入するつもり
name="浅木"
input_scores()
name="松田"
input_scores()

#5-7 引数を受け取るhello関数
def hello(name):
    print(f"{name}")
#5-8 引数を渡しながらhello関数を呼び出す
hello("浅木")
hello("松田")
print()

#5-9 複数の引数を受け取るprofile関数
def profile(name,age,hobby):
    print(f"私の名前は{name}です。")
    print(f"年齢は{age}歳です。")
    print(f"趣味は{hobby}です。")

#5-10 複数の引数を渡しながらprofile関数を呼び出す
profile("浅木",24,"カフェ巡り")


# 5-11 calc_average　既
def calc_average(scores):
    avg = sum(scores)/len(scores)
    print(f"平均点は{avg}です。")
# 5-12 input_scoresとcalc_average 既
def input_scores(name):
    print(f"{name}さんの試験結果を入力してください")
    network = int(input("ネットワークの得点?>>"))
    database = int(input("データベースの得点?>>"))
    security = int(input("セキュリティの得点?>>"))
    scores = [network,database,security]

def calc_average(scores):
    avg = sum(scores)/len(scores)
    print(f"平均点は{avg}です")

# 5-13  input_scores と calc_averageを呼び出す
input_scores("浅木")
#calc_average(scores)

# 5-14 足し算の結果を返すplus関数
def plus(x,y):
    answer = x + y
    return answer

# 5-15 plus関数の呼び出し
answer = plus(100,50)
print(f"足し算の答えは{answer}です")

# 5-16 さまざまな機能を担当する関数の定義
def input_scores(name):
    print(f"{name}さんの試験結果を入力してください")
    network = int(input("ネットワークの得点>>"))
    database = int(input("データベースの得点?>>"))
    security = int(input("セキュリティの得点?>>"))
    scores = [network,database,security]
    return scores

def calc_average(scores):
    avg = sum(scores)/len(scores)
    return avg

def output_result(name,avg):
    print(f"{name}さんの平均点{avg}です")
    

# 5-17 試験結果を入力して平均点を出す
# 浅木と松田の得点入力
asagi_scores = input_scores("浅木")
matsuda_scores = input_scores("松田")
# 平均点を計算
asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)
# 結果を出力
output_result("浅木",asagi_avg)
output_result("松田",asagi_scores)













