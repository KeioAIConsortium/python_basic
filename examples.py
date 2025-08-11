# Page 10 変数
name = "Taro"
age = 17

print(name)
print(age)

# Page 11 変数の型
name = "Taro"
age = 17

print(type(name))
print(type(age))

# Page 12 各データ型
## int, float型
print(3 + 2) # 足し算
print(4 - 1.5) # 引き算
print(2 * 3) # 掛け算
print(10 / 2) # 割り算
print(5 % 2) # 割り算の余り
print(2 ** 3) # べき乗
print((3 + 4) * 2) # 括弧を使った演算

## str型
a = "Hello"
b = "World"
print(a + " " + b) # 文字列を結合

print("Hi!" * 3) # 文字列を繰り返し

word = "Python"
print(len(word)) # 文字列の長さを取得

# Page 13 リスト
fruit = ["apple", "banana", "cherry"]
print(fruit[0])
print(fruit[1])
print(fruit[2])

# Page 14 リストの使用例
scores = [85, 90, 100]
total = scores[0] + scores[1] + scores[2]
average = total / 3
print("Total:", total)
print("Average:", average)

# Page 16 条件式
x = 4
y = 2
print(x == 2)
print(x > y)

# Page 17 if文
x = 2
if x > 3:
    print("xは3より大きい")
else:
    print("xは3以下")

# Page 18 if文2
x = 4
y = 2
if x == y:
    print("等しい")
elif x > y:
    print("xの方が大きい")
else:
    print("yの方が大きい")

# Page 23 dict
taro = {"age": 17, "school": "keio", "club": "soccer"}
print(taro["age"])
print(taro["school"])
print(taro["soccer"])

# Page 24 dictの使用例
students = [
    {
        "name": "keio taro",
        "grade": 2,
        "class": "A"
    },
    {
        "name": "keio hanako",
        "grade": 3,
        "class": "C"
    }
]
print(students[0]["name"])
print(students[1]["grade"])

# Page 27 for文1
for i in range(5):
    print("Hello World")

