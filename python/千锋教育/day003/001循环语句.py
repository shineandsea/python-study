'''
for i in range(n):  ---->固定次数
    pass

while 条件：--->1.固定次数循环 2.不确定次数的循环
    pass

不确定次数的循环
while True:
    pass

'''
'''
掷筛子
两个:1-6
1.玩游戏要有金币，不能玩游戏
2.玩游戏赠金币1枚，充值获取金币
3.10元的倍数，20个金币
4.玩游戏消耗金币5个
5.猜大小：猜对 +2，猜错无奖励；超过6点以上为大，否则为小
6.游戏结束：1.主动退出 2.没有金币退出
7.只要退出则打印金币数，共玩了几局

'''
import time

def f2():#游戏区
    game_01 = '匹配'
    game_02 = '排位'
    game_03 = '休闲区'
    
    while True:
        game_input = input('选择游戏类型:匹配、排位、休闲区、返回菜单\n')
        if game_input == game_01:
            print('匹配中')
            time.sleep(2)
            print('匹配成功')
            pass#游戏内容
            print('game over')
            

        elif game_input == game_02:
            print('匹配中')
            time.sleep(2)
            print('匹配成功')

        elif game_input == game_03:
            print('匹配中')
            time.sleep(2)
            print('欢迎来到休闲区，可以认识更多的小伙伴哦~')
        
        else:
            break

def f1(a):#主菜单
    game = '游戏'
    set = '设置'
    store = '商店'
    top_up = '充值'
    coins = a
    print(coins)
    # coins = 0
    while True:
        select_input = input('选择项目:游戏、设置、商店、充值、退出游戏\n')

        if select_input == game:
            f2()

        elif select_input == set:
            print('set')
            pass#设置内容

        elif select_input == store:
            print('store')
            pass#商店
        
        elif select_input == top_up:
            while True:
                money_input =input('输入充值金额：10；30；50；自定义；退出\n')
                # print(type(int(money_input)))
                
                if money_input == '自定义':
                    while True:
                        money_input02 = int(input('请输入金额：'))
                        if money_input02 % 10 == 0:
                            coins_01 = money_input02 // 10 *20
                            coins = coins + coins_01
                            print('充值成功，剩余硬币：%d' % coins)
                            break
                        else:
                            print('请输入整数：')

                elif money_input =='退出':
                    break

                else: 
                    # if int(money_input) == 10 or int(money_input) == 30 or int(money_input) == 50:
                    coins_01 = int(money_input) // 10 *20
                    coins = coins + coins_01
                    print('充值成功，剩余硬币：%d' % coins)
                    break

        else:
            # print('退出')
            break
     

username = 'mhq'
password = '123'

coin = 0
while True:
    username_input = input('账户:')
    password_input = input('密码:')
    if username_input == username and password_input == password:
        print('登录成功')
        break
    else:
        print('账户或秘密错误')

result = int(input('1:开始游戏;0:退出游戏;'))
if result == True:
    print('欢迎玩家')
    f1(coin)
    print('退出游戏')
else:
    print('退出游戏')
    