#coding=utf-8
import Lib.ClassSelenium as ClassSelenium
global driver
global InputData
global UIExcept

def init():
    global driver
    driver=ClassSelenium.ClassSelenium("http://www.baidu.com")

def login():
    init()
    driver.getelementbyattribute('id:kw').sendkeys(InputData.get('商户名称'))   #��
    driver.getelementbyattribute('id:su').Click()
    aaa=driver.getelementbyattribute('id:kw').getattribute('value')
    driver.close()
    if aaa==UIExcept.get('UICheckOne'):
        return 'Pass',''
    else:
        return 'Fail','is fail'