def f():
    num = int(input())
    

    if 0 <= num <= 20:
        if num >= 0 and num <=10:
            print('welcome user')
        elif num > 10 and num <= 15:
            print('welcome litter boss')
        else :
            print('welcome boss')

    else:
        print('超出范围，请重新输入')
        f()

f()

