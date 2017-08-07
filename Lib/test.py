'''
Created on 2017年8月4日

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
    global driver
    driver=ClassSelenium.ClassSelenium("http://192.168.70.237:8080/am/login.htm,chrome")
    driver.getelementbyattribute("id:vc_op_code").sendkeys('8888')
    driver.getelementbyattribute('id:vc_op_password').sendkeys("123456")   #��
    driver.getelementbyattribute('id:login').Click()
    driver.getelementbyattribute('link text:系统管理').Click()#菜单
    driver.getelementbyattribute('link text:系统配置管理').Click()#菜单
    driver.getelementbyattribute('link text:用户管理').Click()#菜单
    list = driver.getallframe(driver.driver)
    print(list)