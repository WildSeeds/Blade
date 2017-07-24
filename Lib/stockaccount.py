'''
Created on 2017年7月20日

@author: niucx14840
'''
##coding=utf-8
import Lib.ClassSelenium as ClassSelenium
global driver
global  InputData
global UIExcept

def init():
    global driver
    driver=ClassSelenium.ClassSelenium("http://10.20.27.64:8080/am/login.htm,chrome")

def login():
    init()
    driver.getelementbyattribute('id:vc_op_code').sendkeys('8888')   #��
    driver.getelementbyattribute('id:vc_op_password').sendkeys('123456')
    driver.getelementbyattribute('id:login').Click()
   
if __name__ == '__main__':
    login();
    print("wancheng")