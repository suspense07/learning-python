'''
创建代办清单：
1.创建清单字典
2.添加功能（添加任务、查看任务、标记完成、退出）
'''

'''
修复bug：
1.new_task未初始化报错
2.new_task不重复创建，而追加
'''

'''
修复思路：
1.在外部建立字典，直接以任务和0,1的键值对形式构建列表
2.展示任务时，循环打印拼接即可
'''

tasks = {}

while True:
    user_command = input('\n======代办清单======\n1.添加任务\n2.查看任务\n3.标记任务\n4.退出\n请输入对应数字：')
    if user_command == '1':
        task = input('请输入任务内容：')
        # 以 0 表示任务未完成，1 表示任务完成
        tasks[task] = 0
    elif user_command == '2':
        print('===任务总览===')
        for i,task in enumerate(tasks):
            str_task = f'{i+1}.' + task
            if tasks[task] == 1:
                str_task += ' (已完成)'
            print(str_task)
    elif user_command == '3':
        mask_task = input('请输入已完成任务名称：')
        for task in tasks:
            if mask_task in task:
                tasks[task] = 1
    elif user_command == '4':
        break
    else:
        print('请输入正确数字指令')