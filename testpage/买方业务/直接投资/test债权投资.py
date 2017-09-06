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
from Lib.买方业务.直接投资.债权投资 import *
import Lib.买方业务.直接投资.债权投资
import collections
import Lib

import logging

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('webUI.log')
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
#设置输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger = logging.getLogger('testWebUI')
logger.addHandler(fh)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)


def init(xmlpath):

    global InputData
    global UIExcept
    InputData=collections.OrderedDict()
    UIExcept=collections.OrderedDict()
    DOMTree = parse(xmlpath)
    collection = DOMTree.documentElement
    if collection.hasAttribute('note'):
        logger.info('执行案例'+ collection.getAttribute('note'))
    subs =collection.getElementsByTagName('sub')
    num = 1
    sub = subs[0]
    logger.info('执行sub{{0}}:{1}'.format(num,sub.getAttribute('id')))
    num +=1
    ins = sub.getElementsByTagName('inparams')[0].getElementsByTagName('in')
    uis = sub.getElementsByTagName('UIexcept')[0].getElementsByTagName('in')
    for i in ins:
        InputData[i.getAttribute('name')] = i.getAttribute('value')
    for j in uis:
        UIExcept[j.getAttribute('name')] = j.getAttribute('value')

    Lib.买方业务.直接投资.债权投资.UIExcept = UIExcept
    Lib.买方业务.直接投资.债权投资.InputData = InputData


    global driver
    driver=ClassSelenium.ClassSelenium("http://192.168.70.237:8080/am/login.htm,chrome")

    driver.getelementbyattribute("id:vc_op_code").sendkeys(InputData.get('账号'))
    driver.getelementbyattribute('id:vc_op_password').sendkeys(InputData.get('密码'))   #��
    driver.getelementbyattribute('id:login').Click()
    driver.getelementbyattribute('link text:买方业务').Click()#菜单
    driver.getelementbyattribute('link text:直接投资').Click()#菜单
    driver.getelementbyattribute('link text:债权投资').Click()#菜单
    #Lib.买方业务.直接投资.债权投资.driver = driver
    #获取左侧列表

def add():
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\买方业务\直接投资\债权投资合同新增,xml'
        init(xmlpath)
    loanrivalaccount1 = investment(driver)
    loanrivalaccount1.search()
    loanrivalaccount1.add()
def modify():
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\买方业务\直接投资\债权投资合同变更,xml'
        init(xmlpath)
    loanrivalaccount1 = investment(driver)
    loanrivalaccount1.search()
    loanrivalaccount1.modify()
def delete():
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\买方业务\直接投资\债权投资合同变更,xml'
        init(xmlpath)
    loanrivalaccount1 = investment(driver)
    loanrivalaccount1.search()
    loanrivalaccount1.delete()
def settle():
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\买方业务\直接投资\债权投资合同结清.xml'
        init(xmlpath)
    loanrivalaccount1 = investment(driver)
    loanrivalaccount1.search()
    loanrivalaccount1.Popmenu('结清','结清日期','结清日期')
def period():
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\买方业务\直接投资\债权投资合同展期.xml'
        init(xmlpath)
    loanrivalaccount1 = investment(driver)
    loanrivalaccount1.search()
    loanrivalaccount1.Popmenu('展期','项目代码#RD','展期原因')
def classification(): #五级分类
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\买方业务\直接投资\债权投资合同五级分类.xml'
        init(xmlpath)
    loanrivalaccount1 = investment(driver)
    loanrivalaccount1.search()
    loanrivalaccount1.Popmenu('五级分类变更', '项目代码#RD', '变更日期')
def Badassets(): #不良资产核销
    if __name__ == '__main__':
        xmlpath = r'D:\Documents\GitHub\Blade\datapage\买方业务\直接投资\债权投资合同不良资产核销.xml'
        init(xmlpath)
    loanrivalaccount1 = investment(driver)
    loanrivalaccount1.search()
    loanrivalaccount1.Popmenu('不良资产核销', '项目代码#RD', '核销原因')

if __name__ == '__main__':
    Badassets()