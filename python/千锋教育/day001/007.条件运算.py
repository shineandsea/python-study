# money = 100000
# if 1000 < money < 5000:
#     print('奖励1000元！恭喜！')
# elif 5000 < money < 10000:
#     print('jianglibijibenIBM!gongxi!')
# elif 10000 < money < 100000:
#     print('gongxitesila')
# elif money > 100000:
#     print('iphone macbookpro11')
# else:
#     print('maorongwanju')

'''
人工管理系统
'''
def f3():
    result2 = int(input('请选择你的身份'))
    f4()

def f4():
    if result2 == 1:
        
        print(f1)
    elif result2 == 2:
        f2()
    else:
        f3()

def f1():
    class A:
        name:'mhq'
        sex :'男'
        age : 18

def f2():
    class B:
        name:'mxm'
        sex :'男'
        age : 21

print('开机')
result1 = int(input())
if result1 == 1:
    print('欢迎使用管理系统')
result2 = int(input('请选择你的身份'))
f4()



