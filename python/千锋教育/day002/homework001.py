print('欢迎光临')
price = float(input('商品单价'))
number = int(input('商品数量'))
total = price * number
choice = input('选择付款:1、支付宝；2、微信；3、现金；4、刷卡')
if choice == '1':
    total = total - total * 0.1
    print('支付宝支付....')
    print('支付金额是::%.2f' % total)
elif choice == '2':
    print('微信支付')
    total *= 0.95
    print('支付金额为::%.2f' % total)
elif choice == '3':
    print('现金付款没有折扣，应付金额是：%.2f' % total)
elif choice =='4':
    print('刷卡支付')
    if total > 100:
        total -= 20
        print('支付金额是::%.2f' % total)
    else:print('没有折扣，支付金额是::%.2f' % total)
else:
    print('输入错误！~')


