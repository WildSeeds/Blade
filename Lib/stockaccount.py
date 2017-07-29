#coding=utf-8
'''
Created on 2017年7月21日

@author: Administrator
'''

import Lib.ClassSelenium as ClassSelenium
import time
import pickle
from lib2to3.tests.support import driver
from warnings import catch_warnings
global driver
global InputData
global UIExcept


def init():
    global driver
    driver=ClassSelenium.ClassSelenium("http://192.168.70.237:8080/am/login.htm,chrome")
    driver.getelementbyattribute("id:vc_op_code").sendkeys('8888')
    driver.getelementbyattribute('id:vc_op_password').sendkeys("123456")   #��
    driver.getelementbyattribute('id:login').Click()
    driver.getelementbyattribute('link text:系统管理').Click()#菜单
    driver.getelementbyattribute('link text:系统配置管理').Click()#菜单
    driver.getelementbyattribute('link text:用户管理').Click()#菜单
    #获取用户表单
    global operatable
    operatable=driver.getelementbyattribute('tag name:table,id:data_table_dataTable')
    #获取用户功能菜单
    global buttonmenu
    buttonmenu=driver.getelementbyattribute("xpath:.//*[@id='wrap_dataTable']/div[1]")


def end():
    time.sleep(15)
    driver.close()


def clicktable(num=0):
    operatablearray=operatable.getelementbyattribute('tag name:tr',True) #查找所有的行
    operatablearray[num].Click()


def addOp():
    grid9=buttonmenu.getelementbyattribute('link text:新增')
    grid9.Click()
    addwin=driver.getelementbyattribute("id:addWin")
    a=addwin.getelementbyattribute('tag name:input,ref:ztree_vc_branch_id')#获取部门树按钮
    a.Click()
    driver.getelementbyattribute("id:ztree_vc_branch_id_1_a").Click()#点击第一个部门
    addwin.getelementbyattribute('tag name:input,name:vc_op_name').sendkeys("webui")
    addwin.getelementbyattribute('tag name:input,name:vc_bm_name').sendkeys("webui")
    addwin.getelementbyattribute('tag name:button,text:取消').Click()


def modifyOp():
    clicktable(0)
    grid9=buttonmenu.getelementbyattribute('link text:修改')
    grid9.Click()
    addwin=driver.getelementbyattribute("id:editWin")
    a = addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]')
    a.Click()
    driver.getelementbyattribute("id:ztree_vc_branch_id_edit_1_span").Click()
    addwin.getelementbyattribute(
        r'xpath:descendant::label[@title="用户名称"]/following-sibling::*/descendant::*/input[last()]').sendkeys(
        "webui")
    addwin.getelementbyattribute(
        r'xpath:descendant::label[@title="用户别名"]/following-sibling::*/descendant::*/input[last()]').sendkeys(
        "webui")
    addwin.getelementbyattribute(
        r'xpath:descendant::label[@title="电话号码"]/following-sibling::*/descendant::*/input[last()]').sendkeys(
        "webui")
    addwin.getelementbyattribute(
        r'xpath:descendant::label[@title="手机号码"]/following-sibling::*/descendant::*/input[last()]').sendkeys(
        "webui")
    addwin.getelementbyattribute(
        r'xpath:descendant::label[@title="联系地址"]/following-sibling::*/descendant::*/input[last()]').sendkeys(
        "webui")
    addwin.getelementbyattribute(
        r'xpath:descendant::label[@title="电子邮件"]/following-sibling::*/descendant::*/input[last()]').sendkeys(
        "webui")
    addwin.getelementbyattribute(
        r'xpath:descendant::label[@title="身份证号"]/following-sibling::*/descendant::*/input[last()]').sendkeys(
        "webui")
    addwin.getelementbyattribute(
        r'xpath:descendant::label[@title="其他信息"]/following-sibling::*/descendant::*/input[last()]').sendkeys(
        "webui")
    time.sleep(10)
    addwin.getelementbyattribute('tag name:button,text:取消').Click()
    clicktable(0)




def passRest():
    clicktable(0)
    grid9=buttonmenu.getelementbyattribute('link text:密码重置')
    grid9.Click()
    addwin=driver.getelementbyattribute("id:h_msg_floatdiv")
    addwin.getelementbyattribute('tag name:button,text:取消').Click()
    clicktable(0)


def passCancel():
    clicktable(0)
    grid9=buttonmenu.getelementbyattribute('link text:注销')
    grid9.Click()
    addwin=driver.getelementbyattribute("id:logoutWin")
    addwin.getelementbyattribute('tag name:button,text:取消').Click()
    clicktable(0)


def roleApply():
    clicktable(0)
    grid9=buttonmenu.getelementbyattribute('link text:角色分配')
    grid9.Click()
    addwin=driver.getelementbyattribute("id:logoutWin")
    addwin.getelementbyattribute('tag name:button,text:取消').Click()
    clicktable(0)

def exceptioncheck(windriver):
    try:
        windriver.getelementbyattribute(r'css selector:.verify-tip-inner',getall = True)
    except Exception as ex:
        pass
    else:
        raise ClassSelenium.SeleniumError("css.verify-tip-inner:"+"输入值有误")


def login():
    clicktable(0)
    grid9=buttonmenu.getelementbyattribute('link text:修改')
    grid9.Click()
    addwin=driver.getelementbyattribute(r'xpath:/html/body/child::div[@style="display: block;"]/div[2]')
    #/html/body/descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]
    a=addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]')
    a.Click()
    driver.getelementbyattribute("id:ztree_vc_branch_id_edit_1_span").Click()
    #addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]').sendkeys("webui")
    addwin.getelementbyattribute(r'xpath:descendant::label[@title="用户名称"]/following-sibling::*/descendant::*/input[last()]').sendkeys("webui")
    addwin.getelementbyattribute(r'xpath:descendant::label[@title="用户别名"]/following-sibling::*/descendant::*/input[last()]').sendkeys("webui")

    exceptioncheck(addwin)
    addwin.getelementbyattribute('tag name:button,text:确定').Click()
    confirmwin=driver.getelementbyattribute(r"xpath:.//*[@id='h_msg_floatdiv']") #获取弹出的窗体
    confirmwin.getelementbyattribute(r"xpath:.//div[2]/div/div,text:请您确认是否提交？")
    confirmwin.getelementbyattribute('tag name:button,text:确定').Click()
    #addwin.getelementbyattribute('tag name:button,text:取消').Click()
    htip = driver.getelementbyattribute(r"xpath://div[@class='h_tips']")
    htip.getelementbyattribute('tag name:div,text:操作成功！')
    print("操作成功")
    clicktable(0)
    
    time.sleep(10)
    #driver.close()
    #return 'Pass',''
if __name__ == '__main__':
    init()
    login()
    end()