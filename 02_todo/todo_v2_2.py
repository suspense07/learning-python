'''
代办清单文件储存功能优化：
1.每次输入命令后读取修改文件
'''

import json
import os



while True:
    user_command = input('\n======代办清单======\n1.添加任务\n2.查看任务\n3.标记任务\n4.删除任务\n5.退出\n请输入对应数字：')

    # tasks接收json文件
    if os.path.exists('task_sheet.json'):
        with open('task_sheet.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
    else:
        tasks = {}


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

    # tasks转换为json文件
    with open('task_sheet.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)