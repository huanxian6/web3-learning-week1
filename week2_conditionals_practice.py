# -*- coding: utf-8 -*-
"""
================================================================
第 2 周任务：Python 条件语句 · 练习册
================================================================
用法：
  1. 用 VS Code 打开本文件
  2. 右上角点 ▶ 运行，看终端输出
  3. 顺序：先读【一、示例】→ 自己动手做【二、练习】→ 最后对【三、参考答案】

⚠️ 规则：参考答案在文件最底部，先自己写，写完再看。
   报错不是失败，是 Python 在告诉你哪里不懂。
================================================================
"""


# ================================================================
# 一、示例：先跑一遍，再逐行读懂
# ================================================================

print("===== 1. 最基本的 if =====")

score = 85

# 结构：if 条件:
#           要做的事（必须缩进 4 个空格）
# 注意：条件后面有冒号，下一行必须缩进
if score >= 60:
    print("及格了")

# 条件不成立时，整块直接跳过，什么都不输出
if score >= 90:
    print("优秀")        # 85 不满足 >= 90，所以这句不会执行


print("\n===== 2. if / else 二选一 =====")

age = 17

if age >= 18:
    print("成年人")
else:
    print("未成年人")


print("\n===== 3. if / elif / else 多选一 =====")

# 从上往下判断，命中一个就不再往下看
score = 78

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")          # 78 命中这里，输出 C
else:
    print("D")


print("\n===== 4. 比较运算符（结果都是 bool）=====")

a = 10
b = 3

print(f"{a} >  {b}  → {a > b}")       # 大于
print(f"{a} <  {b}  → {a < b}")       # 小于
print(f"{a} >= {b}  → {a >= b}")      # 大于等于
print(f"{a} <= {b}  → {a <= b}")      # 小于等于
print(f"{a} == {b}  → {a == b}")      # 等于（两个等号！）
print(f"{a} != {b}  → {a != b}")      # 不等于


print("\n===== 5. 逻辑运算符 and / or / not =====")

age = 20
has_ticket = True

# and：两个都真才为真
if age >= 18 and has_ticket:
    print("可以入场")

# or：一个真就为真
is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("今天休息")

# not：取反
is_raining = False
if not is_raining:
    print("不用带伞")


print("\n===== 6. 嵌套判断（if 里面还有 if）=====")

score = 85
attendance = 0.9

if score >= 60:
    if attendance >= 0.8:
        print("及格且出勤达标")
    else:
        print("及格但出勤不足")
else:
    print("不及格")


print("\n===== 7. 简写：一行 if / else（三元表达式）=====")

age = 20
status = "成年" if age >= 18 else "未成年"
print(status)

# 等价于：
# if age >= 18:
#     status = "成年"
# else:
#     status = "未成年"


print("\n===== 8. in / not in：判断是否在容器里 =====")

fruits = ["苹果", "香蕉", "橘子"]
print("苹果" in fruits)          # True
print("西瓜" not in fruits)      # True

name = "linkaiyu"
print("lin" in name)             # True，字符串也能判断子串


print("\n===== 9. 判断空值 =====")

username = ""

# 空字符串、0、空列表在条件里都等于 False
if username:
    print(f"欢迎，{username}")
else:
    print("用户名不能为空")


# ================================================================
# 二、练习：每题在下面自己写代码（先别看答案）
# ================================================================

print("\n===== 练习开始 =====\n")

# 【练习 1】判断奇偶
# 输入一个整数，是偶数输出"偶数"，否则输出"奇数"
# 提示：偶数的判断是 num % 2 == 0
num =int(input('请输入一个整数:'))

num % 2 == 0
if num % 2 == 0:
    print('偶数')
else:
    print('奇数')

# 【练习 2】成绩等级
# 输入分数（0-100），输出等级：
#   90 及以上 → A，80-89 → B，60-79 → C，60 以下 → D
# 提示：用 if / elif / else
分数 = int(input('请输入分数:'))
if 分数 >= 90:
    print('A')
elif 分数 >= 80:
    print('B')
elif 分数 >= 60:
    print('c')
else:
    print('D')    


# 【练习 3】闰年判断
# 输入年份，判断是否闰年。规则：
#   能被 4 整除但不能被 100 整除，或者能被 400 整除
# 提示：用 and / or 组合
year = int(input('请输入年份:'))
if (year % 4 ==0 and year %100 !=0) or year % 400 ==0:
    print('闰年')
else:
    print('平年')     


# 【练习 4】登录验证
# 用户名是 "admin" 且密码是 "123456" 时输出"登录成功"，
# 否则输出"用户名或密码错误"


# 【练习 5】判断三角形
# 输入三条边 a、b、c，判断能否构成三角形。
# 规则：任意两边之和大于第三边


# 【练习 6】年龄段
# 输入年龄，输出：0-17 未成年，18-59 成年，60 及以上老年


# 【练习 7】数字大小比较
# 输入三个数字，输出最大的那个（不许用 max 函数）


# 【练习 8】会员折扣
# 输入消费金额和是否会员（y/n）：
#   会员满 100 打 8 折，非会员满 200 打 9 折，其他不打折
# 输出最终应付金额


# ================================================================
# 三、参考答案（先自己写，写完再对）
# ================================================================

"""
【练习 1】
    num = int(input("请输入一个整数："))
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")

【练习 2】
    score = float(input("请输入分数："))
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 60:
        print("C")
    else:
        print("D")

【练习 3】
    year = int(input("请输入年份："))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("闰年")
    else:
        print("平年")

【练习 4】
    username = input("用户名：")
    password = input("密码：")
    if username == "admin" and password == "123456":
        print("登录成功")
    else:
        print("用户名或密码错误")

【练习 5】
    a = float(input("a："))
    b = float(input("b："))
    c = float(input("c："))
    if a + b > c and a + c > b and b + c > a:
        print("能构成三角形")
    else:
        print("不能构成三角形")

【练习 6】
    age = int(input("请输入年龄："))
    if age < 18:
        print("未成年")
    elif age < 60:
        print("成年")
    else:
        print("老年")
    # 注意：这里不用写 age >= 18，因为能走到 elif 说明前面的条件不成立

【练习 7】
    a = float(input("第一个数："))
    b = float(input("第二个数："))
    c = float(input("第三个数："))
    if a >= b and a >= c:
        print(f"最大的是 {a}")
    elif b >= a and b >= c:
        print(f"最大的是 {b}")
    else:
        print(f"最大的是 {c}")

【练习 8】
    amount = float(input("消费金额："))
    is_member = input("是否会员（y/n）：")

    if is_member == "y" and amount >= 100:
        pay = amount * 0.8
    elif is_member == "n" and amount >= 200:
        pay = amount * 0.9
    else:
        pay = amount

    print(f"应付：{round(pay, 2)} 元")
"""


# ================================================================
# 四、常见错误对照表（报错时先来这里查）
# ================================================================
"""
错误 1：if score >= 60      ← 少了冒号
        SyntaxError: expected ':'

错误 2：if score >= 60:
        print("及格")        ← 没有缩进
        IndentationError: expected an indented block

错误 3：if score = 60:      ← 用了一个等号
        SyntaxError: invalid syntax
        正确的是 ==

错误 4：num = input("数字：")
        if num > 10:         ← input 拿到的是字符串
        TypeError: '>' not supported between instances of 'str' and 'int'
        正确：num = int(input("数字："))

错误 5：if "True":          ← 字符串 "True" 不是布尔值，它的值是 True（非空），
                                但判断逻辑容易写错，别这样写

记住：
  - 条件后面一定有冒号 :
  - 下一行一定缩进 4 个空格
  - 判断相等用 ==，赋值用 =
  - input() 的结果要 int() / float() 转换
"""


# ================================================================
# 五、学完自检（不看资料，能全部做到就算过关）
# ================================================================
"""
[ ] 写出 if / if-else / if-elif-else 三种结构，都不查资料
[ ] 说出 == 和 = 的区别
[ ] 用 and / or / not 各写一个条件
[ ] 写出判断闰年的条件
[ ] 解释为什么 if 后面要缩进
[ ] 不看答案，独立完成练习 1-5

全部打勾 → 回规划看板，把「Python 条件语句」任务勾掉 ✅
"""
