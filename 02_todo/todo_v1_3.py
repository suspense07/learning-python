'''
创建代办清单：
1.创建清单字典
2.添加功能（添加任务、查看任务、标记完成、退出）
3.增加一个删除功能
'''


tasks = {}

while True:
    user_command = input('\n======代办清单======\n1.添加任务\n2.查看任务\n3.标记任务\n4.删除任务\n5.退出\n请输入对应数字：')
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
        if mask_task in tasks.keys():
            tasks[mask_task] = 1
    elif user_command == '4':
        del_task = input('请输入需要删除的任务名称：')
        if del_task in tasks.keys():
            del tasks[del_task]
    elif user_command == '5':
        break
    else:
        print('请输入正确数字指令')