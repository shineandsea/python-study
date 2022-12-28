n = 1
while n <= 10:
    print('------>n=%d' % n)
    n += 1

'''
1、打印1-50直接能被3整除的数
2、1-10累加和
'''
n = 1
while n < 50 :
    if n % 3 == 0:
        print('n=%d' % n)
    n += 1

n = 1
sum = 0
while n <= 10:
    sum += n
    n += 1
print('1-10累加sum=%d' %sum)
 