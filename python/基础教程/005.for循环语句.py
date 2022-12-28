#遍历
for letter in 'python':
    print('字母',letter)

arr = ['mhq','mxm','wx']
for array in arr:
    print('ren',array)

#通过索引迭代
fruits = ['banana','apple','mangguo']
for index in range(len(fruits)):
    print(fruits[index])


for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num/i
            print('%d = %d * %d'%(num,i,j))
            break
    else:
        print('%d is a zhishu'%num)

        
        