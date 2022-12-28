total = 0
flag = 1
while flag:
    price = float(input('输入价格:'))
    number = int(input('输入数量'))
    #累加
    total += price * number

    #判断是否继续购买
    answer = input('当前商品总额为：%.2f,是否继续购买(q表示退出)?' % total)
    if answer == 'q':
        flag = 0
    

print('所有商品金额为：%.2f' % total)



