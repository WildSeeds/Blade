'''
Created on 2017骞�8鏈�4鏃�

@author: niucx14840
'''
import Lib.ClassSelenium as ClassSelenium
from Lib.ClassSelenium import ElementObject
import time
from warnings import catch_warnings
from _ast import Num
from xml.dom.minidom import parse
import xml.dom.minidom

global driver
global InputData
global UIExcept

if __name__ == '__main__':
    InputData={}
    UIExcept={}
    DOMTree = parse(r'D:\Documents\GitHub\Blade\datapage\基础信息\对手方账号维护\loanaccountadd.xml')
    collection = DOMTree.documentElement
    if collection.hasAttribute('note'):
        print(collection.getAttribute('note'))
    subs =collection.getElementsByTagName('sub')
    for sub in subs:
        ins = sub.getElementsByTagName('inparams')[0].getElementsByTagName('in')
        uis = sub.getElementsByTagName('UIexcept')[0].getElementsByTagName('in')
        for i in ins:
            InputData[i.getAttribute('name')] = i.getAttribute('value')
        #print(InputData)
        for j in uis:
            UIExcept[j.getAttribute('name')] = j.getAttribute('value')
        #print(UIExcept)

        