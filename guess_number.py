"""
猜数字小游戏（可以反复玩）
规则：电脑随机生成 1-100 之间的整数，玩家最多猜 7 次。
      每次猜错都会提示"大了"或"小了"，猜对则通关。
      一局结束后输入 y 再来一局，输入其他内容退出。
运行：点 VS Code 右上角 ▶，然后在终端里输入数字并回车。
"""

import random

# 外层循环：一局玩完后再回到这里，就是"再来一局"
while True:
    # ===== 一局开始：重新生成答案、把计数清零 =====
    answer = random.randint(1, 100)   # 每局都要换一个答案

    max_attempts = 7      # 最多允许猜的次数
    attempts = 0          # 已猜次数
    guessed = False       # 是否猜中

    print("=" * 32)
    print("  猜数字游戏：我心里有个 1-100 的数")
    print(f"  你最多可以猜 {max_attempts} 次")
    print("=" * 32)

    # ===== 内层循环：这一局怎么猜 =====
    while attempts < max_attempts and not guessed:
        guess = int(input("请输入你猜的数字："))
        attempts += 1

        if guess == answer:
            guessed = True
            print(f"🎉 猜对了！答案就是 {answer}")
            print(f"你一共用了 {attempts} 次")
        elif guess > answer:
            print(f"大了！还剩 {max_attempts - attempts} 次机会")
        else:
            print(f"小了！还剩 {max_attempts - attempts} 次机会")

    # ===== 这一局结束，结算 =====
    if not guessed:
        print(f"😢 机会用完了，正确答案是 {answer}")

    # ===== 问要不要再来一局 =====
    again = input("再来一局？（输入 y 继续，其他任意键退出）：")
    if again.lower() != "y":
        print("游戏结束，下次再玩！")
        break
