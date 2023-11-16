
"""
#practice 5-1
def weather():
def calc_circle_area(herf_circle_Size):
def nowstr():
def nowint():
def is_leapyear(current_year):
"""
# 5-2
def is_leapyear(current_year):
    if current_year % 400 ==0:
        return True
    if current_year % 4 ==0:
        if not current_year %100 ==0:
            return True
year= int(input("現在の西暦を入力してください"))

result= is_leapyear(year)

if result:
    print(f"{year}は、うるう年です")
else:
    print(f"{year}は、うるう年ではありません")

# 5-3
"""
def run():
    walk()
    print("ちょっと歩きます")
    
"""

# 5-4
"""
(1)
× 
英語にはデフォルト引数が指定されている
(2)
△
可変長引数の定義が謎 for文などでotherが適切に展開されるなら〇
(3)
〇
(4)
〇
(5)
〇
"""
# 5-5
"""ベース
#計算データの入力
amount = int(input("支払総額を入力してください"))
people = int(input("参加人数を入力してください"))
#割り勘の計算
dnum = amount /people
pay = dnum // 100*100
if dnum > pay:
    pay = int(pay +100)

#幹事の支払額の計算
payorg = amount - pay *(people - 1)

#結果の表示
print("*** 支払額 ***")
print(f"1人あたり{pay}円({people}人)、幹事は{payorg}円です")

"""


def int_input(str):
    inputNum = int(input(f"{str}を入力してください"))
    return inputNum

def clac_payment(amount,people=2):
    dnum= amount / people
    #2222 /2 = 1111
    pay = dnum // 100*100
    #1.1 
    #1100
    if dnum > pay:
        pay = int(pay +100)
    #1200

    payorg = amount - pay *(people - 1)
    # 2222 - 1200 * 1 = 1022
    return (pay,payorg)

def show_payment(pay,payorg,people=2):
    print("*** 支払額 ***")
    print(f"1人あたり{pay}円({people}人)、幹事は{payorg}円です")


#main
amount = int_input("支払総額")
people = int_input("参加人数")

(pay,payorg) = clac_payment(amount,people)

show_payment(pay,payorg,people)
