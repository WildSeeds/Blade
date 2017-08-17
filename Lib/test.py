'''
Created on 2017骞�8鏈�4鏃�

@author: niucx14840
'''
import Lib.ClassSelenium as ClassSelenium
from Lib.ClassSelenium import ElementObject
import time
from warnings import catch_warnings
from _ast import Num
global driver
global InputData
global UIExcept

if __name__ == '__main__':
    a ='请您确认是否提交'
    b = '请您确认是否提交?'
    if a  in b:
        print('in')
    else:
        print('not in')