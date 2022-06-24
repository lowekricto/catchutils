# -*- coding: utf-8 -*-
# COMMAND 002
# 保存动漫
import threading
import time
import os
import urllib
import urllib.request
import requests


# 任务数
TASK_ALL = 0
TASK_NOW = 0
TASK_FINISH = 0

# 线程数
THREAD_MAX = 10
THREAD_RUNN = 0

# 运行flag

POOL_IS_RUNNING = False

#
lock = threading.Lock()

# 任务列表
TASK_LIST = []

HEADER = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36',
}
###############################################################


def taskstart():
    global TASK_ALL, TASK_NOW, THREAD_RUNN

    TASK_NOW += 1
    THREAD_RUNN += 1


def taskFinish():
    global TASK_ALL, TASK_NOW, TASK_FINISH
    global THREAD_RUNN
    TASK_NOW -= 1
    TASK_FINISH += 1
    THREAD_RUNN -= 1


def nowtask():
    global TASK_ALL, TASK_NOW, TASK_FINISH
    ret = '正在进行的任务数：'+str(TASK_NOW)+'\n'+'全部的任务数：' + \
        str(TASK_ALL)+'\n'+'已完成的任务数：'+str(TASK_FINISH)+'\n'

    return ret


def getatask():
    global TASK_LIST

    ret = []

    lock.acquire()

    ret = TASK_LIST[0]
    del TASK_LIST[0]

    lock.release()

    return ret


def getcount(list):
    index = 0
    for x in list:
        index += 1
    return index


##############################################################

def bodytotasklist(body):
    # 0@top 执行top
    # 1@task&folderpath~url*path~ff 下载命令
    global TASK_LIST, TASK_ALL

    tasks = []
    fullpath = ''

    fristCommand = str(body).split('@')
    if(fristCommand[0] == '0'):
        ret = nowtask()
        return ret
    elif(fristCommand[0] == '1'):
        secondCommand = fristCommand[1].split('&')
        if(secondCommand[0] == 'task'):
            thirdCommand = secondCommand[1].split('~')
            # 存储路径
            fullpath = thirdCommand[0]
            checked = os.path.exists(fullpath)
            if(not checked):
                os.makedirs(fullpath)

            del thirdCommand[0]
            for x in thirdCommand:
                # x[0] url
                # x[1] filename
                if(x == 'ff'):
                    break
                t = x.split('*')
                tasks = [t[0], t[1]]
                TASK_LIST.append(tasks)

            TASK_ALL += getcount(TASK_LIST)

            return '任务发送完毕'
        else:
            return '任务发送失败'


def threadSave():
    task = getatask()
    url = task[0]
    path = task[1]
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(url, path)
    taskFinish()


def threadSend():
    global THREAD_RUNN, THREAD_MAX, TASK_LIST, POOL_IS_RUNNING
    print('Mession Pool flow')

    POOL_IS_RUNNING = True

    while(1):

        count = getcount(TASK_LIST)

        if(count == 0):

            time.sleep(1)
            continue

        if(THREAD_RUNN < THREAD_MAX):
            # 开启新线程
            taskstart()
            t = threading.Thread(target=threadSave, args=())
            t.start()


# ! 测试指令
def main(body):
    global POOL_IS_RUNNING

    ret = ''

    # 解析命令
    ret = bodytotasklist(body)

    # 运行后台
    if(POOL_IS_RUNNING):
        return ret

    t = threading.Thread(target=threadSend, args=())
    t.start()

    return ret
