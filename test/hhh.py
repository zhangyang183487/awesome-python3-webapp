#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from multiprocessing import Process


def run_childProcess(name):
    print('Run Child process %s (%s)...' % (name, os.getpid()));


if __name__ == '__main__':
    print('Parent process %s ...' % (os.getpid()));

    # 创建子进程时，只需要传入一个执行函数和函数的参数
    p = Process(target=run_childProcess, args=('test',));

    print('Child process will start.')

    # 创建一个Process实例，用start()方法启动
    p.start();

    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join();

    print('Child process end.')
