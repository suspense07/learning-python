'''
创建代办清单：
1.创建清单列表
2.添加功能（添加任务、查看任务、标记完成、退出）
'''



tasks = []

while True:
    user_command = input('\n======代办清单======\n1.添加任务\n2.查看任务\n3.标记任务\n4.退出\n请输入对应数字：')
    if user_command == '1':
        task = input('请输入任务内容：')
        tasks.append(task)
        # 以 0 表示任务未完成，1 表示任务完成
        new_tasks = {f'{i+1}.{task}': 0 for i,task in enumerate(tasks)}
    elif user_command == '2':
        str_task = '\n'.join([i[0] if i[1] == 0 else i[0] + ' (已完成)' for i in new_tasks.items()])
        print('===任务总览===\n' + str_task)
    elif user_command == '3':
        mask_task = input('请输入已完成任务名称：')
        for task in new_tasks:
            if mask_task in task:
                new_tasks[task] = 1
    elif user_command == '4':
        break
    else:
        print('请输入正确数字指令')