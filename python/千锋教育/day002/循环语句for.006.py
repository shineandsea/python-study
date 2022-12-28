'''
for (){
    循环体
}

for 变量名 in range()

'''
sum = 0
for i in range(1,50,5):
    sum += i
print('sum=',sum)

##账户登录
for i in range(3):
    username = input('用户名')
    password = input('密码')
    if username == 'mhq' and password =='123321':
        print('登陆成功')
        break
    else:
        if i == 2:
            print('已输入三次，账户锁定')
        else:
            print('账户或密码错误，还有%d次机会'%(2-i))
        
