#产生随机数
import random
ran = random.randint(1,50)
count = 0
while True:
    guess = int(input('猜一个1-50之间的数字:'))
    count += 1
    if guess == ran:
        if count == 1:
            print('恭喜猜对啦！')
        else:
            print('运气还不错！')
        break
    elif guess > ran:
        print('猜大了！')
    else:
        print('猜小了！')

