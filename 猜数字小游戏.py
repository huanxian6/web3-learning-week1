import random
while True:
    答案 = random.randint(1,100)
    最大次数 = 7
    已猜次数 = 0
    是否正确 = False
    print("="*32)
    print('猜数字游戏:我心里有一个1~100的数')
    print(f'你最多能猜{最大次数}次')
    print('='*32)
    while 已猜次数 < 最大次数 and not 是否正确:
        数字 = int(input(f'请输入你猜的数字：'))
        if 数字 <1 or 数字 >100:
            print('数字无效,请输入1~100之间的数字')
        else:
            已猜次数 += 1
            if  数字 == 答案:
                是否正确 = True
                print('恭喜你猜对了！')
                print(f' 你一共用了{已猜次数}次')
            elif 数字 < 答案:
                print('小了！')
                print(f'还剩{最大次数 - 已猜次数}次机会')
            elif 数字 > 答案:
                print('大了！')
                print(f'还剩{最大次数 - 已猜次数}次机会')
            else:
                print(f'游戏结束，次数耗尽！正确答案为：{答案}')
    再来 = input('是否再来一局 ?(y继续,其他键退出）:')
    if 再来 != 'y':
        print('欢迎下次再来')
        break