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
from Lib.基础信息管理.对手方信息.对手方账户维护 import *
import Lib.基础信息管理.对手方信息.对手方账户维护
import collections
import Lib




def init(xmlpath):
    
    global InputData
    global UIExcept
    InputData=collections.OrderedDict()
    UIExcept=collections.OrderedDict()
    DOMTree = parse(xmlpath)
    collection = DOMTree.documentElement
    if collection.hasAttribute('note'):
        print('执行案例',collection.getAttribute('note'))
    subs =collection.getElementsByTagName('sub')
    num = 1
    for sub in subs:
        print('执行sub{{0}}:{1}'.format(num,sub.getAttribute('id')))
        num +=1
        ins = sub.getElementsByTagName('inparams')[0].getElementsByTagName('in')
        uis = sub.getElementsByTagName('UIexcept')[0].getElementsByTagName('in')
        for i in ins:
            InputData[i.getAttribute('name')] = i.getAttribute('value')
        for j in uis:
            UIExcept[j.getAttribute('name')] = j.getAttribute('value')

        Lib.基础信息管理.对手方信息.对手方账户维护.UIExcept = UIExcept
        Lib.基础信息管理.对手方信息.对手方账户维护.InputData = InputData

        
    global driver
    driver=ClassSelenium.ClassSelenium("http://192.168.70.237:8080/am/login.htm,chrome")

    driver.getelementbyattribute("id:vc_op_code").sendkeys(InputData.get('账号'))
    driver.getelementbyattribute('id:vc_op_password').sendkeys(InputData.get('密码'))   #��
    driver.getelementbyattribute('id:login').Click()
    driver.getelementbyattribute('link text:基础信息管理').Click()#菜单
    driver.getelementbyattribute('link text:对手方信息').Click()#菜单
    driver.getelementbyattribute('link text:对手方账户维护').Click()#菜单
    
    Lib.基础信息管理.对手方信息.对手方账户维护.driver = driver
    #获取左侧列表

def add():
    xmlpath = r'D:\Documents\GitHub\Blade\datapage\基础信息\对手方账号维护\loanaccountadd.xml'
    init(xmlpath)
    loanrivalaccount1 = loanrivalaccount(driver)
    #loanrivalaccount1.search()
    loanrivalaccount1.add()
def modify():
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\基础信息\对手方账号维护\loanaccountmodify.xml'
        init(xmlpath)
    loanrivalaccount1 = loanrivalaccount(driver)
    # loanrivalaccount1.search()
    loanrivalaccount1.modify()
def delete():
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\基础信息\对手方账号维护\loanaccountdelete.xml'
        init(xmlpath)
    loanrivalaccount1 = loanrivalaccount(driver)
    loanrivalaccount1.delete()
if __name__ == '__main__':
    add()