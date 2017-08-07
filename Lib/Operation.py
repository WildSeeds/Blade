﻿#coding=utf-8
import Lib.ClassSelenium as ClassSelenium
import time
global driver
global InputData
global UIExcept

def init():
    global driver
    driver=ClassSelenium.ClassSelenium("http://10.20.27.63:8080/am/login.htm,chrome")

def login():
    init()
    driver.getelementbyattribute('css selector:#vc_op_code').sendkeys(InputData.get('商户名称')) #获取案例值
    driver.getelementbyattribute('css selector:#vc_op_password').sendkeys("123456")   #��
    driver.getelementbyattribute('css selector:#login').Click()
    driver.getelementbyattribute('link text:投资管理').Click()#菜单
    driver.getelementbyattribute('link text:债权投资').Click()#菜单
    driver.getelementbyattribute('class name:g-unit-wrap,text:投资明细代码').getelementbyattribute('name:vc_stock_code,type:text').sendkeys("ZQD10061700W")
    driver.getelementbyattribute('tag name:button,text:查询').Click()
    driver.movetoelement(driver.getelementbyattribute("xpath:.//*[@id='tr_dataTable_1']/td[3]/div/div"))
    driver.getelementbyattribute("xpath:.//*[@id='body_dataTable']/ul/li[1]/a").Click()
    driver.getelementbyattribute('css selector:#vc_product_id_zqtz>.u-select.m-verify-success').sendkeys("500028-基金恒业")
    #driver.getelementbyattribute('css selector:#combi_id_zqtz>.u-select.m-verify-success').Select("2:缺省组合")
    #driver.getelementbyattribute('css selector:#combi_id_zqtz>.u-select.m-verify-success').Select("2:缺省组合")
    driver.getelementbyattribute("xpath:.//*[@id='tab1_zqtz']/form/div[2]/button[1]").Click()
    aaa=driver.getelementbyattribute("xpath:.//*[@id='h_msg_floatdiv']/div[2]/div").gettext()
    driver.getelementbyattribute("xpath:.//*[@id='buttonCancel']").Click()
    print(aaa)
    print(UIExcept.get('UICheckOne'))
    if aaa==UIExcept.get('UICheckOne'):#UI检查
        return 'Pass',''
    else:
        return 'Fail','is fail'
    driver.close()
    #return 'Pass',''