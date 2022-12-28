username = input('用户名')
password = input('密码')
is_remember = False
if username == 'admin' and password =='1234':
    if is_remember:
        print('已经记住用户%s的密码啦' % username)
        