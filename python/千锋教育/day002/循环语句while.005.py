import random
n=1
p_count = 0
m_count = 0
while n <= 3:
    ran = random.randint(0,2)
    guess = int(input('请输入你的(0-剪刀，1-石头，2-布)'))
    if (ran==0 and guess==2 or ran==1 and guess==0 or ran==2 and guess==1):
        print('本局败北')
        p_count += 1
    elif (guess==0 and ran==2 or guess==1 and ran==0 or guess==2 and ran==1):
        print('本局胜利')
        m_count += 1
    else :
        print('本局平局')
    n += 1

if p_count > m_count:
    print('败北')
elif p_count < m_count:
    print('胜利')
else:
    print('平局')  


