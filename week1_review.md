# 第 1 周复盘 · 启动期

> 用时 30 分钟｜对应任务：`【复盘】本周总结 + 代码 push 到 GitHub 第一个仓库`（10 XP）
> 用法：直接在 `[ ]` 里打 x 填成 `[x]`，空白横线处写自己的话，然后把这个文件一起提交到 GitHub。

## 一、任务清点（5 分钟）

对着看板一条条过，做到就打 `[x]`。**没做完的不要删，标"待补"写进第四部分。**

- [x] 周六｜安装 Python + VS Code，跑通 Hello World
- [x] 周六｜注册 GitHub 账号，知道 GitHub 是干什么的
- [x] 周日｜B站：区块链是什么（动画）
- [x] 周日｜浏览 Web3 项目生态全景
- [x] 周一｜Python 变量与数据类型（int/str/float/bool）
- [x] 周一｜编程核心术语 20 个
- [x] 周二｜字符串操作 + input() 用户输入
- [x] 周二｜区块链 100 问 前 5 集
- [x] 周三｜条件语句 if / elif / else
- [x] 周三｜区块链核心术语 20 个
- [x] 周四｜循环 for / while + range()
- [x] 周四｜英语高频词 Day1（30 个）
- [x] 周五｜猜数字游戏（if + while）
- [x] 周五｜本周复盘 + 代码 push 到 GitHub

完成数：____ / 14　　XP：____ / 2xx

## 二、四个问题（10 分钟，每题 2-3 句就够）

**1. 这周真正学会了什么？**
（只写"能关掉教程独立写出来"的，不写"看过/知道"的）

- 容易忘，可能需要多复习

**2. 卡最久的是哪一步？最后怎么解决的？**

- while循环，看ai提供的步骤解决，但感觉又不太会

**3. 犯过的错里，哪个最典型？现在再遇到还会不会犯？**
（提示：NameError 变量没定义 / ValueError 类型转不了 / SyntaxError 全角标点 / 代码输进了终端）

- 老是忘记加：‘等标点符号

**4. 下周只改一件事，改什么？**

- 记得加标点符号

## 三、本周代码清单（整理 5 分钟）

把这周写过的 `.py` 文件挑出来，重命名成能看懂的名字，再放进一个 `week1` 文件夹。

| 文件                                 | 作用                          | 是否要改名字                                |
| ---------------------------------- | --------------------------- | ------------------------------------- |
| `week1_variables_practice.py`      | 变量与数据类型练习                   | 不用                                    |
| `week2_conditionals_practice.py`   | 条件语句练习（虽然叫 week2，其实是第1周周三的） | 建议改成 `week1_conditionals_practice.py` |
| `guess_number.py`                  | 猜数字游戏（可重玩）                  | 不用                                    |
| `python.py`                        | 第一次测试变量和 type()             | 可以删掉或合并                               |
| `test.py` / `is_at_school=true.py` | 早期试手的小文件                    | 可以删掉                                  |
| `num % 2 == 0.py`                  | 奇偶判断 → 后来改成登录判断             | 改成 `login.py`                         |

> 原则：**文件名里不要放代码**（空格、`%`、`=`、`==` 都会给以后的工具链添麻烦），只用英文小写 + 下划线。

## 四、下周 3 个目标（5 分钟）

1. 
2. 
3. 

## 五、本周遗留问题

| 问题  | 打算什么时候补   |
| --- | --------- |
| 1   | 每周规定时间内完成 |
|     |           |

---

## 附：GitHub 首次提交命令（PowerShell）

```powershell
# 1. 在项目文件夹里初始化仓库
git init

# 2. 让 __pycache__ 不被提交
"__pycache__/" | Out-File -Encoding utf8 .gitignore

# 3. 添加全部文件
git add .

# 4. 提交（第一次必须设置身份，把邮箱和名字换成你自己的）
git config user.email "你的邮箱@example.com"
git config user.name "你的名字"
git commit -m "第1周：Python基础练习与猜数字游戏"

# 5. 关联远程仓库并推送（地址换成你自己仓库的）
git branch -M main
git remote add origin https://github.com/你的用户名/仓库名.git
git push -u origin main
```

第一次 `git push` 会弹浏览器让你登录 GitHub，登录一次以后就不用再登了。
