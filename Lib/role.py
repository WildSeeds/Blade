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
    driver.getelementbyattribute('link text:角色管理').Click()#菜单
    #获取左侧列表
class role(object):
    def __init__(self,window):
        self.window = window
        self.upwindow=driver.getelementbyattribute('tag name:form,name:queryForm')
        self.downwindow = driver.getelementbyattribute('id:wrap_dataTable')
        self.dialog_message = driver.getelementbyattribute('id:dialog-message',getall=True)[0]
        self.dialog_message_confirmnex = driver.getelementbyattribute('id:dialog_message_confirmnext',getall=True)[0]
        
        

        
    # 点击展开按钮并做检查 

    def search(self,value=''):
        self.upwindow.getelementbyattribute('tag name:button,text:清空').Click()
        a = self.upwindow.getelementbyattribute(r'xpath:descendant::label[@title="角色名称"]/following-sibling::*/descendant::*/input[last()]')
        if notemptycheck(a):
            raise ClassSelenium.SeleniumError("角色搜索清空失败")
        a.sendkeys(value)
        self.upwindow.getelementbyattribute('tag name:button,text:查询').Click()
    
        
    def end(self):
        time.sleep(15)
        driver.close()
    
      
    def add(self):
        self.downwindow.getelementbyattribute('link text:新增').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.downwindow.getelementbyattribute('link text:新增').Click()
        #/html/body/descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]
        addwin.getelementbyattribute(r'xpath:descendant::label[@title="角色编号"]/following-sibling::*/descendant::*/input[last()]').sendkeys('3')
        addwin.getelementbyattribute(r'xpath:descendant::label[@title="角色名称"]/following-sibling::*/descendant::*/input[last()]').sendkeys("3")
        addwin.getelementbyattribute(r'xpath:descendant::label[@title="备注"]/following-sibling::*/descendant::*/input[last()]').sendkeys("webui")
        exceptioncheck(addwin)
        addwin.getelementbyattribute('tag name:button,text:确定').Click()
        msgfloat(driver,'确认','请您确认是否提交','取消','角色新增')
        addwin.getelementbyattribute('tag name:button,text:确定').Click()
        msgfloat(driver,'确认','请您确认是否提交','确定','角色新增')
        htips(driver,'操作成功');
        self.search()
    
    def modify(self):
        SelectListData(driver,'角色名称','3')
        self.downwindow.getelementbyattribute('link text:修改').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.downwindow.getelementbyattribute('link text:修改').Click()
        #/html/body/descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]
        v1 = addwin.getelementbyattribute(r'xpath:descendant::label[@title="角色编号"]/following-sibling::*/descendant::*/input[last()]')
        v2 = addwin.getelementbyattribute(r'xpath:descendant::label[@title="角色名称"]/following-sibling::*/descendant::*/input[last()]')
        v3 = addwin.getelementbyattribute(r'xpath:descendant::label[@title="备注"]/following-sibling::*/descendant::*/input[last()]')
        if not readonly(v1):
            raise ClassSelenium.SeleniumError("角色编号非只读")
        v2.clear()
        v2.sendkeys(3)
        v3.clear()
        v3.sendkeys('webui')
        exceptioncheck(addwin)
        addwin.getelementbyattribute('tag name:button,text:确定').Click()
        msgfloat(driver,'确认','请您确认是否提交','取消','角色修改')
        addwin.getelementbyattribute('tag name:button,text:确定').Click()
        msgfloat(driver,'确认','请您确认是否提交','确定','角色修改')
        htips(driver,'操作成功');
        self.search()
    def delete(self):
        SelectListData(driver,'角色名称','3')
        self.downwindow.getelementbyattribute('link text:删除').Click()
        msgfloat(driver,'确认','请您确认是否删除','取消','角色删除')
        self.downwindow.getelementbyattribute('link text:删除').Click()
        msgfloat(driver,'确认','请您确认是否删除','确定','角色删除')
        htips(driver,'操作成功');
        self.search()
    
  
    def rolemanageadd(self):
        SelectListData(driver,'角色名称','3')
        self.window.getelementbyattribute('link text:批量分配角色').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.window.getelementbyattribute('link text:批量分配角色').Click()
        
        opbranch =  branchmanager(driver,addwin)
        opbranch.search()
        opstr = 'webui用户webui'     #sendkey
        opbranch.check()
        opbranch.branchadd(opstr)
        msgfloat(driver,'提示','操作成功','确定','批量分配角色')
        
    def rolemanagedel(self):
        SelectListData(driver,'部门简称','二级部门')
        self.downwindow.getelementbyattribute('link text:部门经理指定').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.downwindow.getelementbyattribute('link text:部门经理指定').Click()
        
        opbranch =  branchmanager(driver,addwin)
        opbranch.search()
        opstr = 'webui用户webui'     #sendkey
        opbranch.branchdelet(opstr)
        msgfloat(driver,'提示','操作成功','确定','部门管理员任命')
        clicktable(0)
        grid9=buttonmenu.getelementbyattribute('link text:角色分配')
        grid9.Click()
        addwin=driver.getelementbyattribute("id:logoutWin")
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        clicktable(0)
    


    
    
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

class  branchmanager(object):
    def __init__(self,driver,window):
        self.driver = driver
        self.window = window
        container = window.getelementbyattribute('css selector:.sortable_container')
        divlist = container.getelementbyattribute('xpath:div',getall =True)
        self.divletf = divlist[0]
        self.divadd = divlist[1]
        self.divdel = divlist[2]
        self.divrigt = divlist[3]
        self.allchooseleft = self.divletf.getelementbyattribute('xpath:.//span[text()="列名"]/preceding-sibling::input')
        self.allchooseright = self.divrigt.getelementbyattribute('xpath:.//span[text()="列名"]/preceding-sibling::input')
        
    def getunchooselist(self):
        try :
            temp1 = self.divletf.getelementbyattribute('tag name:li',getall =True)
            unchooselit = [(x.getelementbyattribute('tag name:input,type:checkbox'),x.gettext())  for x in temp1]
        except Exception as e:
            print(e)
            unchooselit = []
        return unchooselit

    def getchooselist(self):
        try :
            temp2 =  self.divrigt.getelementbyattribute('tag name:li',getall =True)
            chooselit = [(x.getelementbyattribute('tag name:input,type:checkbox'),x.gettext())  for x in temp2]
        except :
            chooselit = []
        return chooselit
    
    def search(self):
        v1 = self.window.getelementbyattribute(r'xpath:descendant::label[@title="用户编号"]/following-sibling::*/descendant::*/input[last()]')
        v2 = self.window.getelementbyattribute(r'xpath:descendant::label[@title="用户名称"]/following-sibling::*/descendant::*/input[last()]')
        v3 = self.window.getelementbyattribute(r'xpath:descendant::label[@title="部门名称"]/following-sibling::*/descendant::*/input[last()]') 
        v1.clear()
        v1.sendkeys('')  
        v2.clear()
        v2.sendkeys('')
        v3.sendkeys('webUI')
        #b = driver.getelementbyattribute('id:hc_hide_div-tree-vc_branch_id_opbquery1')
        b = driver.getelementbyattribute(r'css selector:.hc_selectbox-tree-div,style:[\s\S]*display: block;')
       
        c = b.getelementbyattribute(r'xpath:descendant::a[@title="'+'webUI'+'"]/preceding-sibling::span[last()-1]')
        c.Click()
        self.window.getelementbyattribute('tag name:button,text:查询').Click()
    def branchadd(self,opstr):

        oplist = opstr.split(',')
        unchooselist = self.getunchooselist()
        chooselist=self.getchooselist()
        print('unchooselist',unchooselist)
        print('chooselist',unchooselist)
        for i in oplist:
            for j in unchooselist:
                if i == j[1]:
                    print(i,'vs',j[1])
                    j[0].Click()
                    continue
                raise ClassSelenium.SeleniumError('添加用户:未找到对应用户:',j[1])
        self.divadd.Click()
        afterunchooselist = self.getunchooselist()
        afterchooselist=self.getchooselist()
        if (len(unchooselist)-len(afterunchooselist)) == len(oplist) or (len(afterchooselist)-len(chooselist)) == len(oplist):
            for i in oplist:
                for j in afterchooselist:
                    if i == j[1]:
                        continue
                    raise ClassSelenium.SeleniumError('添加用户:已选列表未包含对应用户:',j[1])
            for i in oplist:
                for j in afterunchooselist:
                    if i == j[1]:
                        raise ClassSelenium.SeleniumError('添加用户:未选列表仍包含对应用户:',j[1])
        else:
            raise ClassSelenium.SeleniumError('添加用户:添加用户已选和未选数量变化不正确')
        self.window.getelementbyattribute('tag name:button,text:确定').Click()    
    def branchdelet(self,opstr):
        oplist = opstr.split(',')
        # 为了简化修改，和add保持一致，把list数据进行对掉
        chooselist = self.getunchooselist()
        unchooselist=self.getchooselist()
        
        for i in oplist:
            for j in unchooselist:
                if i == j[1]:
                    print('找到了',j[1])
                    j[0].Click()
                    continue
                raise ClassSelenium.SeleniumError('添加用户:未找到对应用户:',j[1])
        self.divdel.Click()
        afterchooselist = self.getunchooselist()
        afterunchooselist=self.getchooselist()
        if (len(unchooselist)-len(afterunchooselist)) == len(oplist) or (len(afterchooselist)-len(chooselist)) == len(oplist):
            for i in oplist:
                for j in afterchooselist:
                    if i == j[1]:
                        continue
                    raise ClassSelenium.SeleniumError('添加用户:已选列表未包含对应用户:',j[1])
            for i in oplist:
                for j in afterunchooselist:
                    if i == j[1]:
                        raise ClassSelenium.SeleniumError('添加用户:未选列表仍包含对应用户:',j[1])
        else:
            raise ClassSelenium.SeleniumError('添加用户:添加用户已选和未选数量变化不正确')
        self.window.getelementbyattribute('tag name:button,text:确定').Click()
    def clear(self):
        self.window.getelementbyattribute('tag name:button,text:清空').Click()
        chooselist=self.getchooselist()
        if len(chooselist) !=0:
            raise ClassSelenium.SeleniumError('清空用户信息:清空失败')
  
    def check(self):
        self.clear()
        self.divadd.Click()
        htips(self.window,'请至少选择一条记录')
        self.divdel.Click()
        htips(self.window,'请至少选择一条记录')
        
   
      
if __name__ == '__main__':
    init()
    role1 =role(driver)
    role1.search()
    #role1.add()
    #role1.modify()
    #role1.delete()
    role1.rolemanageadd()
    #role1.delete()
    
    role1.end()