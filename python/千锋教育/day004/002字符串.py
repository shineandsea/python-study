'''
http://renzhouyixun.oa.wanmei.net/training/image/new-logo.png?version=0.4634713452878454
'''
path = 'http://renzhouyixun.oa.wanmei.net/training/image/new-logo.png?version=0.4634713452878454'

#find,index,rfind,rindex
#从左到右
i = path.find('/')
print(i)
image_name = path[i+1:]
print(image_name)

#从右到左
j = path.rfind('o')
print(i)
image_name = path[j:]
print(image_name)
