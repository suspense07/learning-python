'''
猜数字小游戏：
1.生成1-100间的随机数字
2.用户输入一个数字
3.如果用户输入的数字大于随机数，提示用户猜大了
4.如果用户输入的数字小于随机数，提示用户猜小了
5.如果用户输入的数字等于随机数，提示用户猜对了
'''

import random


random_number = random.randint(1,100)

while True:
    user_number = int(input('请输入1-100的数字：'))
    if user_number > random_number:
        print('猜大了')
    elif user_number < random_number:
        print('猜小了')
    else:
        print('猜对了')
        break


