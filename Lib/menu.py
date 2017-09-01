#coding=utf-8
'''
Created on 2017年7月21日

@author: Administrator
'''

import Lib.ClassSelenium as ClassSelenium
import time
import pickle
import builtins
#from lib2to3.tests.support import driver
from warnings import catch_warnings
global driver
global InputData
global UIExcept

class menu(object):
    def __init__(self,menuwindow,leaf):
        self.leaf =leaf
        self.menuself = menuwindow
        self.menulink = self.getmenulink()
        self.name =self.getname()
        self.submenulist =self.submenu()
    def getmenulink(self):
        if self.leaf > 0:
            return self.menuself.getelementbyattribute(r'xpath:a')
        else:
            return None
    def getname(self):
        if self.leaf > 0:
            return self.menulink.gettext()
        else:
            return "主菜单"
    def submenu(self):
        if self.leaf > 0:
            try:
                menuelelist = self.menuself.getelementbyattribute(r'xpath:ul/li',getall = True)
            except Exception:
                return None
        else:
            try:
                menuelelist =  self.menuself.getelementbyattribute(r'xpath:li',getall = True)
            except Exception:
                return None
        return menuelelist
    def openallmenu(self):
        for i in self.submenulist:
            j = menu(i,1)
            j.getmenulink().Click();
            #time.sleep(1)
            if j.submenulist:
                for k in j.submenulist:
                    m = menu(k,2)
                    m.getmenulink().Click();
                    #time.sleep(1)
                    if m.submenulist:
                        for n in m.submenulist :
                            p = menu(n,3)
                            p.getmenulink().Click();
                            #time.sleep(1)

            
            
            
class menunavigation(object):
    def __init__(self,driver):
        self.driver = driver
        self.menunavigationself =self.driver.getelementbyattribute(r'css selector:.h-screen-tab')
        self.forward = menunavigation.getelementbyattribute('xpath:div[1]')
        self.label=menunavigation.getelementbyattribute('xpath:div[2]')
        self.backward = menunavigation.getelementbyattribute('xpath:div[3]')
        self.zoom = menunavigation.getelementbyattribute('xpath:div[4]')
        self.View_toolbar = menunavigation.getelementbyattribute('xpath:div[5]')
    def getmenutable(self,name): 
        tabellist = self.label.getelementbyattribute('tag name:li',getall = True) #获取标签页按钮
        for i in tabellist:
            tabelspan = i.getelementbyattribute('tag name:span',getall = True)
            if tabelspan[0].gettext() == name:
                if len(tabelspan) > 1:
                    return (tabelspan[0],tabelspan[1])
                else:
                    return (tabelspan[0],None)
        return None
            
    def getcloseTab(self):
        self.View_toolbar.Click()
        return self.View_toolbar.getelementbyattribute('tag name:a',getall =True)
        
        

def init():
    global driver
    driver=ClassSelenium.ClassSelenium("http://10.20.25.124:8080/am/login.htm,chrome")
    driver.getelementbyattribute("id:vc_op_code").sendkeys('yq124')
    driver.getelementbyattribute('id:vc_op_password').sendkeys("123456")   #��
    driver.getelementbyattribute('id:login').Click()
    menubody = driver.getelementbyattribute(r'css selector:.h-menu-body>ul')
    navigation = driver.getelementbyattribute(r'css selector:.h-screen-tab')
    temtable = menunavigation(navigation)
    a = temtable.getmenutable('主页')
    a[0].Click()
    print(a[0].gettext())
    #fbmenu = menu(menubody,0)
    #fbmenu.openallmenu()
    driver.getelementbyattribute('link text:系统管理').Click()#菜单
    driver.getelementbyattribute('link text:系统配置管理').Click()#菜单
    driver.getelementbyattribute('link text:用户管理').Click()#菜单
    b = temtable.getcloseTab()[0].Click()
    i =0
    while i<5:
        i+=1
        temtable.zoom.Click()
        time.sleep(1)
        temtable.zoom.Click()
if __name__ == '__main__':
    init()
    
    pass