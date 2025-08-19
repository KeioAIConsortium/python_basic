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
average = total / len(scores)
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

# Page 29 for文3
## 0始まり
for i in range(5):
    print(i)

## 1始まり
for i in range(1, 6):
    print(i)

# Page 30 for文4
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

# Page 31 for文5
## break
for i in range(5):
    if i == 2:
        break
    print(i)

## continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# Page 32 for quiz 
## sum
sum = 0
for i in range(10):
    sum = sum + i + 1
print(sum)

# Page 33
for i in range(5):
    print("Hello")

# Page 34
for i in range(10):
    print(i)
    if i == 2:
        continue
    elif i == 8:
        break
print(end)

# Page 36 input関数
text = input()
print("文字列", text, "が変数「text」に保存されました")

num = int(input())
print("整数", num, "が変数「num」に保存されました")

# Page 40
def add1(x):
    result = x + 1
    return result
re = add1(3)
print(re)

# Page 41
## without function
x = 3
x = x * 2
x = x + 1
print(x)

x = 5
x = x * 2
x = x + 1
print(x)

## with function
def calc(x):
    x = x * 2
    x = x + 1
    print(x)

calc(3)
calc(5)

# Page 42
def add(x, y):
    return x + y
a = add(3,4)
print(a)

# Page 43
def daikei(jotei, katei, takasa):
    return (jotei + katei) * takasa / 2
b = daikei(6, 8, 10)
print(b)

# Page 45
def average(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum / len(array)
array([2, 3, 4])
