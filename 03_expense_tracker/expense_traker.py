'''
记账小程序：
1.创建记账列表
2.添加记账本功能（1.添加消费，2.查看所有消费，3.按类别统计，4.退出）
'''

import ast


book = []
rough_book = {}

while True:
    user_command = (input('\n====== 记账本 ======\n1.添加消费\n2.查看所有消费\n3.按类别统计\n4.退出\n请输入对应数字：'))
    if user_command == '1':
        consume_category = input('请输入消费类别：')
        money = ast.literal_eval(input('请输入金额：'))
        book.append((consume_category, money))
        if consume_category not in rough_book.keys():
            rough_book[consume_category] = money
        else:
            rough_book[consume_category] += money
    elif user_command == '2':
        print('=== 详细消费 ===')
        for i,cost_tup in enumerate(book):
            print(f'{i+1}.' + cost_tup[0] + ' - ' + f'{cost_tup[1]} 元')
    elif user_command == '3':
        print('=== 类别消费 ===')
        for i,consume_category in enumerate(rough_book):
            print(f'{i+1}.' + consume_category + ' - ' + str(rough_book[consume_category]) + ' 元')
    elif user_command == '4':
        break
    else:
        print('请输入正确的数字')