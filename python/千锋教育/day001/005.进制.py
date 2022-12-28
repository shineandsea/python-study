'''
二进制0~1
八进制0~7
10进制0~9
16进制0~15
'''
'''
10进制转二进制,n/2取余，反向写
二进制转十进制，系数x2的幂

'''
n = 32
result = bin(n)#2
print(result)

result = oct(n)#8
print(result)

result = hex(n)#16
print(n)

result = bin(n)#10
print(n)

n = 0x558
result = oct(n)
print(result)