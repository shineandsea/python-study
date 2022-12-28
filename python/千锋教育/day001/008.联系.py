username = 'shilong'
total = 1500#消费金额
money = 0
coupon = 0#优惠券

if 0 <total <500:
    quan1 = random.randint(1,10)
    quan2 = random.randint(1,10)
    quan3 = random.randint(1,10)
    coupon = quan1  + quan2 + quan3

elif 500 <= total < 2000:
    coupon += 2*50
    recharge = input('%s,是否要充值(充值送10%)(y/n)')
    if recharge =='y':
        money += 1.1*int(input('充值金额'))
        

elif total >=2000:
    pass
