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
    #driver.getelementbyattribute('link text:部门管理').Click()#菜单
    driver.getelementbyattribute(r"xpath://div[2]/div[1]/div/div[3]/ul/li[13]/ul/li[1]/ul/li[10]/a").click()
    #获取左侧列表
class branch(object):
    def __init__(self):
        self.leftwindow=driver.getelementbyattribute('id:branchForm')
        self.rightwindow = driver.getelementbyattribute('id:wrap_branchTable')
        self.dialog_message = driver.getelementbyattribute('id:dialog-message',getall=True)[0]
        self.dialog_message_confirmnex = driver.getelementbyattribute('id:dialog_message_confirmnext',getall=True)[0]
        
        

        
    # 点击展开按钮并做检查 
    def Unfolded(self):
        self.leftwindow.getelementbyattribute('link text:展开').Click()
        try:
            self.leftwindow.getelementbyattribute('tag name:span,class:button level\d* switch noline_close',getall = True,TIMEOUT=5)
            raise ClassSelenium.SeleniumError("switch noline_open"+"折叠展开失败")
        except Exception :
            pass
    # 点击收缩按钮并做检查 
    def folded(self):
        self.leftwindow.getelementbyattribute('link text:收缩').Click()
        try:
            self.leftwindow.getelementbyattribute('tag name:span,class:button level\d* switch noline_open',getall = True,TIMEOUT=5)
            raise ClassSelenium.SeleniumError("switch noline_close"+"折叠收缩失败")
        except Exception :
            pass
    def search(self):
        a = self.leftwindow.getelementbyattribute('id:search_vc_branch_id')
        a.sendkeys('二级部门')
        b = self.leftwindow.getelementbyattribute('tag name:a,class:level\d* curSelectedNode')
        b.getelementbyattribute(r'xpath:preceding-sibling::span[last()-1]').Click()
        b.Click()
        self.leftwindow.getelementbyattribute('tag name:button,text:查询').Click()
    
        
    def end(self):
        time.sleep(15)
        driver.close()
    
    

    
    def addOp(self):
        self.rightwindow.getelementbyattribute('link text:新增').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.rightwindow.getelementbyattribute('link text:新增').Click()
        #/html/body/descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]
        addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]').sendkeys('3')
        addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门编码"]/following-sibling::*/descendant::*/input[last()]').sendkeys("3")
        addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门简称"]/following-sibling::*/descendant::*/input[last()]').sendkeys("webui")
        addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门全称"]/following-sibling::*/descendant::*/input[last()]').sendkeys("webui")
        a=addwin.getelementbyattribute(r'xpath:descendant::label[@title="上级部门"]/following-sibling::*/descendant::*/input[last()]').sendkeys("二级部门")
        treebranch = driver.getelementbyattribute('tag name:div,ref_target:ztree_vc_parent_branch_id')
        treebranch.getelementbyattribute('tag name:span,text:二级部门').Click()
        exceptioncheck(addwin)
        addwin.getelementbyattribute('tag name:button,text:确定').Click()
        
        #弹出提示信息begin
        h_msg_floatdiv = driver.getelementbyattribute('id:h_msg_floatdiv',getall=True)[0]
        title = h_msg_floatdiv.getelementbyattribute('css selector:.m-message-header').gettext()
        body = h_msg_floatdiv.getelementbyattribute('css selector:.m-body-words').gettext()
        footer = h_msg_floatdiv.getelementbyattribute('css selector:.h_btndiv.m-message-footer').gettext()
        if title != '提示' or body != '操作成功' :
            raise ClassSelenium.SeleniumError("部门增加失败，原因:"+"body")
        h_msg_floatdiv.getelementbyattribute('tag name:button,text:确定').Click();
        #弹出提示信息end
        
        self.leftwindow.getelementbyattribute('tag name:button,text:查询').Click()
    
    def modifyOp(self):
        SelectListData(driver,'部门简称','webui')
        self.rightwindow.getelementbyattribute('link text:修改').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.rightwindow.getelementbyattribute('link text:修改').Click()
        
        #/html/body/descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]
        v1 = addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门编号"]/following-sibling::*/descendant::*/input[last()]')
        v2 = addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门编码"]/following-sibling::*/descendant::*/input[last()]')
        v3 = addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门简称"]/following-sibling::*/descendant::*/input[last()]')
        v4 = addwin.getelementbyattribute(r'xpath:descendant::label[@title="部门全称"]/following-sibling::*/descendant::*/input[last()]')
        v5 = addwin.getelementbyattribute(r'xpath:descendant::label[@title="创建日期"]/following-sibling::*/descendant::*/input[last()]')
        if not readonly(v1,v5):
            raise ClassSelenium.SeleniumError("部门修改表单字段属性非只读")
        v2.clear()
        v2.sendkeys('3')
        v3.clear()
        v3.sendkeys('webui')
        v4.clear()
        v4.sendkeys('webui')
        branchname = "二级部门"
        a=addwin.getelementbyattribute(r'xpath:descendant::label[@title="上级部门"]/following-sibling::*/descendant::*/input[last()]').sendkeys(branchname)
        treebranch = driver.getelementbyattribute('tag name:div,ref_target:ztree_vc_parent_branch_id_edit')
        treebranch.getelementbyattribute('tag name:span,text:'+branchname).Click()
        exceptioncheck(addwin)
        addwin.getelementbyattribute('tag name:button,text:确定').Click()
        #弹出提示信息begin
        h_msg_floatdiv = driver.getelementbyattribute('id:h_msg_floatdiv',getall=True)[0]
        title = h_msg_floatdiv.getelementbyattribute('css selector:.m-message-header').gettext()
        body = h_msg_floatdiv.getelementbyattribute('css selector:.m-body-words').gettext()
        footer = h_msg_floatdiv.getelementbyattribute('css selector:.h_btndiv.m-message-footer').gettext()
        if title != '提示' or body != '操作成功' :
            raise ClassSelenium.SeleniumError("部门修改失败，原因:"+body)
        h_msg_floatdiv.getelementbyattribute('tag name:button,text:确定').Click();
        #弹出提示信息end
        self.leftwindow.getelementbyattribute('tag name:button,text:查询').Click()
        
    def writeoff(self):
        SelectListData(driver,'部门简称','webui')
        self.rightwindow.getelementbyattribute('link text:注销').Click()
        
        #弹出提示信息begin
        h_msg_floatdiv = driver.getelementbyattribute('id:h_msg_floatdiv',getall=True)[0]
        h_msg_floatdiv.getelementbyattribute('tag name:button,text:取消').Click();
        #弹出提示信息end
        
        self.rightwindow.getelementbyattribute('link text:注销').Click()
        
        #弹出提示信息begin
        h_msg_floatdiv = driver.getelementbyattribute('id:h_msg_floatdiv',getall=True)[0]
        title = h_msg_floatdiv.getelementbyattribute('css selector:.m-message-header').gettext()
        body = h_msg_floatdiv.getelementbyattribute('css selector:.m-body-words').gettext()
        footer = h_msg_floatdiv.getelementbyattribute('css selector:.h_btndiv.m-message-footer').gettext()
        if title != '提示' or body != '您确定要注销部门吗' :
            raise ClassSelenium.SeleniumError("部门注销失败，原因:"+body)
        h_msg_floatdiv.getelementbyattribute('tag name:button,text:确定').Click();
        #弹出提示信息end
        
        #弹出提示信息begin
        h_msg_floatdiv = driver.getelementbyattribute('id:h_msg_floatdiv',getall=True)[0]
        title = h_msg_floatdiv.getelementbyattribute('css selector:.m-message-header').gettext()
        body = h_msg_floatdiv.getelementbyattribute('css selector:.m-body-words').gettext()
        footer = h_msg_floatdiv.getelementbyattribute('css selector:.h_btndiv.m-message-footer').gettext()
        if title != '提示' or body != '操作成功' :
            raise ClassSelenium.SeleniumError("部门注销失败，原因:"+body)
        h_msg_floatdiv.getelementbyattribute('tag name:button,text:确定').Click();
        #弹出提示信息begin
        
        self.leftwindow.getelementbyattribute('tag name:button,text:查询').Click()
    
    def departmentmanageradd(self):
        SelectListData(driver,'部门简称','二级部门')
        self.rightwindow.getelementbyattribute('link text:部门经理指定').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.rightwindow.getelementbyattribute('link text:部门经理指定').Click()
        
        opbranch =  branchmanager(driver,addwin)
        opbranch.search()
        opstr = 'webui用户webui'     #sendkey
        opbranch.check()
        opbranch.branchadd(opstr)
        msgfloat(driver,'提示','操作成功','确定','部门管理员任命')
        
    def departmentmanagdel(self):
        SelectListData(driver,'部门简称','二级部门')
        self.rightwindow.getelementbyattribute('link text:部门经理指定').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.rightwindow.getelementbyattribute('link text:部门经理指定').Click()
        
        opbranch =  branchmanager(driver,addwin)
        opbranch.search()
        opstr = 'webui用户webui'     #sendkey
        opbranch.branchdelet(opstr)
        msgfloat(driver,'提示','操作成功','确定','部门管理员任命')
    
    def Leaderschargeadd(self):
        SelectListData(driver,'部门简称','二级部门')
        self.rightwindow.getelementbyattribute('link text:分管领导指定').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.rightwindow.getelementbyattribute('link text:分管领导指定').Click()
        
        opbranch =  branchmanager(driver,addwin)
        opbranch.search()
        opstr = 'webui用户webui'     #sendkey
        opbranch.check()
        opbranch.branchadd(opstr)
        msgfloat(driver,'提示','操作成功','确定','分管领导指定')
        
    def Leaderschargedel(self):
        SelectListData(driver,'部门简称','二级部门')
        self.rightwindow.getelementbyattribute('link text:分管领导指定').Click()
        addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
        addwin.getelementbyattribute('tag name:button,text:取消').Click()
        self.rightwindow.getelementbyattribute('link text:分管领导指定').Click()
        
        opbranch =  branchmanager(driver,addwin)
        opbranch.search()
        opstr = 'webui用户webui'     #sendkey
        opbranch.branchdelet(opstr)
        msgfloat(driver,'提示','操作成功','确定','分管领导指定')
      


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
        v3 = self.window.getelementbyattribute(r'xpath:descendant::label[@title="用户部门"]/following-sibling::*/descendant::*/input[last()]') 
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
                raise ClassSelenium.SeleniumError('添加部门管理员:未找到对应部门:',j[1])
        self.divadd.Click()
        afterunchooselist = self.getunchooselist()
        afterchooselist=self.getchooselist()
        if (len(unchooselist)-len(afterunchooselist)) == len(oplist) or (len(afterchooselist)-len(chooselist)) == len(oplist):
            for i in oplist:
                for j in afterchooselist:
                    if i == j[1]:
                        continue
                    raise ClassSelenium.SeleniumError('添加部门管理员:已选列表未包含对应部门:',j[1])
            for i in oplist:
                for j in afterunchooselist:
                    if i == j[1]:
                        raise ClassSelenium.SeleniumError('添加部门管理员:未选列表仍包含对应部门:',j[1])
        else:
            raise ClassSelenium.SeleniumError('添加部门管理员:添加部门经理已选和未选数量变化不正确')
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
                raise ClassSelenium.SeleniumError('添加部门管理员:未找到对应部门:',j[1])
        self.divdel.Click()
        afterchooselist = self.getunchooselist()
        afterunchooselist=self.getchooselist()
        if (len(unchooselist)-len(afterunchooselist)) == len(oplist) or (len(afterchooselist)-len(chooselist)) == len(oplist):
            for i in oplist:
                for j in afterchooselist:
                    if i == j[1]:
                        continue
                    raise ClassSelenium.SeleniumError('添加部门管理员:已选列表未包含对应部门:',j[1])
            for i in oplist:
                for j in afterunchooselist:
                    if i == j[1]:
                        raise ClassSelenium.SeleniumError('添加部门管理员:未选列表仍包含对应部门:',j[1])
        else:
            raise ClassSelenium.SeleniumError('添加部门管理员:添加部门经理已选和未选数量变化不正确')
        self.window.getelementbyattribute('tag name:button,text:确定').Click()
    def clear(self):
        self.window.getelementbyattribute('tag name:button,text:清空').Click()
        chooselist=self.getchooselist()
        if len(chooselist) !=0:
            raise ClassSelenium.SeleniumError('清空部门人员信息:清空失败')
  
    def check(self):
        self.clear()
        self.divadd.Click()
        htips(self.window,'请至少选择一条记录')
        self.divdel.Click()
        htips(self.window,'请至少选择一条记录')
        


if __name__ == '__main__':
    init()
    branch1 =branch()
    branch1.Unfolded()
    branch1.folded()
    branch1.search()
    #branch1.addOp()
    #branch1.writeoff()
    branch1.Leaderschargeadd()
    
    branch1.end()