# *_*coding:utf-8 *_*
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from src import task1
from src import task2
from src import task3
if __name__ == '__main__':
    task1.task1()
    task2.task2()
    task3.task3()
