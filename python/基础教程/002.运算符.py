#位运算
a = 0b10101001
print(a>>2)
a = a>>2
print(a>>2)
print(a)

a = ~a
print(a)

# 成员运算符
list = [1,2,3,4,5,6]
if(a in list):
    print(a in list)
else:
    print('a not in list' )
b = a
#python身份运算符
if(a is b):
    print('a 与 b 有相同标识')

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个（同一块内存空间），==用于判断变量的值是都相等

c = list[:]
print(c)
b = c[:]
print(b == c)
print(b is c)

'''
    ** 指数
    ~+- 按位翻转
    */%// 乘，除，取模和取整除
    +- 加法减法
    >><< 右移，左移运算符
    & 位'AND'
    ^|位运算符
    <=<>>= 比较运算符
    = %= /= //= -= += *= **= 赋值运算
    is is not 身份运算符
    in not in 成员运算符
    not and or 逻辑运算符

'''
