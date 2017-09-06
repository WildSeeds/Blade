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


class investment(object):
    def __init__(self,driver):
        self.driver = driver
        self.upwindow = self.driver.getelementbyattribute('id:queryForm')
        self.downwindow = self.driver.getelementbyattribute('id:wrap_dataTable')
        self.loanform = form(self.driver, self.upwindow)
    def search(self,value=''):
        self.driver.getelementbyattribute('tag name:button,text:清空').Click()
        loanform = form(self.driver,self.driver)

        if not notemptycheck(loanform['投资明细代码'],loanform['基金代码'],loanform['基金名称'],loanform['投资明细编号'],loanform['投资明细名称']):
            raise ClassSelenium.SeleniumError("投资业务清空搜索条件失败")

        setvalue(loanform,InputData,'投资明细代码_s','投资明细名称_s')

        self.upwindow.getelementbyattribute('tag name:button,text:查询').Click()


    def end(self):
        time.sleep(15)
        driver.close()


    def add(self):
        self.downwindow.getelementbyattribute('link text:新增').Click()
        #切换框架_begin
        self.driver.driver.switch_to_default_content()
        framelist = self.driver.getallframe(self.driver.driver)
        self.driver.switchtoframe(framelist[-1])
        # 切换框架_end
        addwin = self.driver.getelementbyattribute('xpath://div[@class="g-screen"]/descendant::form')
        loanform = form(self.driver,addwin)
        #loanform.printlabel(xml=True)
        setvalue(loanform,InputData,'项目代码','备注信息')
        #loanform.setvalue('省份','32:江苏省')
        #loanform.setvalue('城市','3201:南京市')
        loanform.button('确定')
        msgfloat(self.driver,'确认','请您确认是否提交','否','投资合同新增')
        loanform.button('确定')
        msgfloat(self.driver,'确认','请您确认是否提交','是', '投资合同新增')
        msgfloat(self.driver,'提示','操作成功！投资明细代码为','否', '投资合同新增成功设置利率')
        return


    def modify(self):
        self.downwindow.getelementbyattribute('link text:变更').Click()
        htips(self.driver,'请选择一条记录')
        SelectListData(self.driver,InputData.get('表格选择列名'),InputData.get('表格选择列值'),action='Select')
        self.downwindow.getelementbyattribute('link text:变更').Click()
        # 切换框架_begin
        switchlabelifram(self.driver)
        # 切换框架_end
        addwin = self.driver.getelementbyattribute('xpath://div[@class="g-screen"]/descendant::form')
        loanform = form(self.driver, addwin)
        # loanform.printlabel(xml=True)
        setvalue(loanform, InputData, '项目代码', '备注信息')
        # loanform.setvalue('省份','32:江苏省')
        # loanform.setvalue('城市','3201:南京市')
        loanform.button('确定')
        msgfloat(self.driver, '确认', '请您确认是否提交', '否', '投资合同变更')
        loanform.button('确定')
        msgfloat(self.driver, '确认', '请您确认是否提交', '是', '投资合同变更')
        msgfloat(self.driver, '提示', '操作成功', '确定', '投资合同变更')
        return

    def delete(self):
        self.downwindow.getelementbyattribute('link text:撤销').Click()
        htips(self.driver, '请选择一条记录')
        SelectListData(self.driver, InputData.get('表格选择列名'), InputData.get('表格选择列值'), action='Select')
        self.downwindow.getelementbyattribute('link text:撤销').Click()
        # 切换框架_begin
        switchlabelifram(self.driver)
        # 切换框架_end
        addwin = self.driver.getelementbyattribute('xpath://div[@class="g-screen"]/descendant::form')
        loanform = form(self.driver, addwin)
        # loanform.printlabel(xml=True)
        #setvalue(loanform, InputData, '项目代码', '备注信息')
        # loanform.setvalue('省份','32:江苏省')
        # loanform.setvalue('城市','3201:南京市')
        loanform.button('确定')
        msgfloat(self.driver, '确认', '请您确认是否提交', '否', '投资合同撤销')
        loanform.button('确定')
        msgfloat(self.driver, '确认', '请您确认是否提交', '是', '投资合同撤销')
        msgfloat(self.driver, '提示', '操作成功', '确定', '投资合同变更')
        return
    def Popmenu(self,menu,begin,end):   #结清操作

        menubutton = self.downwindow.getelementbyattribute('link text:{0}'.format(menu))
        menubutton.Click()
        htips(self.driver, '请选择一条记录')
        SelectListData(self.driver,InputData.get('表格选择列名'), InputData.get('表格选择列值'),action='Select')
        menubutton.Click()
        #获取弹窗并进行相关操作_begin
        popwindow(self.driver,menu,'取消')
        menubutton.Click()
        addwin=popwindow(self.driver,menu)
        # 获取弹窗并进行相关操作_end
        loanform = form(self.driver, addwin)
        setvalue(loanform,InputData,begin,end)
        loanform.button('确定')
        msgfloat(self.driver, '确认', '请您确认是否提交', '否', '投资合同'+menu)
        loanform.button('确定')
        msgfloat(self.driver, '确认', '请您确认是否提交', '是', '投资合同'+menu)
        msgfloat(self.driver, '提示', '操作成功', '确定', '投资合同'+menu)
        return






