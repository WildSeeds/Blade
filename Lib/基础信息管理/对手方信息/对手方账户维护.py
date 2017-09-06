#coding=utf-8
'''
Created on 2017年7月21日

@author: Administrator
'''

import Lib.ClassSelenium as ClassSelenium
import time
from Lib.Public import *
from warnings import catch_warnings
from Lib.Common import TIMEOUT
from array import array
from msilib.schema import Class
from lib2to3.fixer_util import String
import Lib

global driver
global InputData
global UIExcept

class loanrivalaccount(object):
    def __init__(self,driver):
        self.driver = driver
        self.loanform = form(self.driver,self.driver)
        self.upwindow = self.driver.getelementbyattribute('id:bankaccountForm')
        self.downwindow = self.driver.getelementbyattribute('id:wrap_bankaccountTable')
    def search(self,value=''):
        self.driver.getelementbyattribute('tag name:button,text:清空').Click()
        loanform = form(self.driver,self.driver)

        if notemptycheck(loanform['对手序号'],loanform['对手简称'],loanform['银行账号']):
            raise ClassSelenium.SeleniumError("角色搜索清空失败")
        print(InputData)

        setvalue(loanform,InputData,'对手序号_s','对手方账户状态_s')

        self.upwindow.getelementbyattribute('tag name:button,text:查询').Click()


    def end(self):
        time.sleep(15)
        driver.close()


    def add(self):
        self.downwindow.getelementbyattribute('link text:新增').Click()
        addwin = driver.getelementbyattribute(r'xpath://body/div[@style="display: block;"]/div[2]')
        driver.getelementbyattribute('tag name:button,text:取消').Click()
        self.downwindow.getelementbyattribute('link text:新增').Click()
        addwin = driver.getelementbyattribute(r'xpath://body/div[@style="display: block;"]/div[2]')
        
        
        
        loanform = form(driver,addwin)
        loanform['对手序号']
        setvalue(loanform,InputData,'对手名称','是否内部账户')
        #loanform.setvalue('省份','32:江苏省')
        #loanform.setvalue('城市','3201:南京市')
        loanform.button('确定')
        msgfloat(self.driver,'提示','操作成功','确定','对手方账号新增')
        return
    

    def modify(self):
        SelectListData(self.driver,InputData.get("表格列名"),InputData.get("表格列值"))
        self.downwindow.getelementbyattribute('link text:修改').Click()
        addwin = driver.getelementbyattribute(r'xpath://body/div[@style="display: block;"]/div[2]')
        driver.getelementbyattribute('tag name:button,text:取消').Click()
        self.downwindow.getelementbyattribute('link text:修改').Click()
        addwin = driver.getelementbyattribute(r'xpath://body/div[@style="display: block;"]/div[2]')

        loanform = form(driver,addwin)
        v1 = loanform['对手名称']
        v2 = loanform['银行总行']
        v3 = loanform['银行账户']
        if not readonly(v1,v2,v3):
            raise ClassSelenium.SeleniumExceptions('对手方账号修改字段非只读')
        
        setvalue(loanform,InputData,'银行名称','是否内部账户')
        
        loanform.button('确定')
        msgfloat(self.driver,'提示','操作成功','确定','对手方账号修改')
        return
    
    def delete(self):
        SelectListData(self.driver, InputData.get("表格列名"), InputData.get("表格列值"))
        self.downwindow.getelementbyattribute('link text:删除').Click()
        msgfloat(driver,'提示','您确定要删除对手方账户吗','取消','对手方账户删除')
        self.downwindow.getelementbyattribute('link text:删除').Click()
        msgfloat(driver, '提示', '您确定要删除对手方账户吗', '确定', '对手方账户删除')
        htips(driver,'操作成功');






