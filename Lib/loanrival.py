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
global driver
global InputData
global UIExcept



def init():
    global driver
    driver=ClassSelenium.ClassSelenium("http://192.168.70.237:8080/am/login.htm,chrome")
    driver.getelementbyattribute("id:vc_op_code").sendkeys('8888')
    driver.getelementbyattribute('id:vc_op_password').sendkeys("123456")   #��
    driver.getelementbyattribute('id:login').Click()
    driver.getelementbyattribute('link text:基础信息管理').Click()#菜单
    driver.getelementbyattribute('link text:对手方信息').Click()#菜单
    driver.getelementbyattribute('link text:对手方维护').Click()#菜单
    #获取左侧列表
class loanrival(object):
    def __init__(self,window):
        self.window = window
        self.upwindow=driver.getelementbyattribute('tag name:form,name:bankaccountForm')
        self.downwindow = driver.getelementbyattribute('id:wrap_bankaccountTable')
        self.dialog_message = driver.getelementbyattribute('id:dialog-message',getall=True)[0]
        self.dialog_message_confirmnex = driver.getelementbyattribute('id:dialog_message_confirmnext',getall=True)[0]
         # 点击展开按钮并做检查

    def search(self,value=''):
        self.upwindow.getelementbyattribute('tag name:button,text:清空').Click()
        loanform = form(driver,self.upwindow)
        if notemptycheck(loanform['对手序号']):
            raise ClassSelenium.SeleniumError("角色搜索清空失败")
        loanform.setvalue('对手序号', '1233')
        loanform.setvalue('对手简称', '1233')
        loanform.setvalue('对手方名称', '1233')
        loanform.setvalue('行业类别', '1:基础产业')
        loanform.setvalue('企业特征','2:大型企业')
        #loanform.setvalue('对手序号', '1233')
        self.upwindow.getelementbyattribute('tag name:button,text:查询').Click()
    
        
    def end(self):
        time.sleep(15)
        driver.close()
    
      
    def add(self):
        self.downwindow.getelementbyattribute('link text:新增').Click()
        driver.driver.switch_to_default_content()
        framelist=driver.getallframe(driver.driver)
        print(framelist)
        #loanform.setvalue['对手简称']

        driver.switchtoframe(framelist[-1])
        addwindow = driver.getelementbyattribute('tag name:form,name:addForm')
        driver.getelementbyattribute('tag name:button,text:重置').Click()
        loanform = form(driver,addwindow)
        # loanform.printlabel()
        # return
        loanform.setvalue('对手简称', 'webUI')
        loanform.setvalue('对手方名称', 'webUI')
        loanform.setvalue('对手类型', '非金融机构')
        loanform.setvalue('角色分类', '抵、质押担保方')
        # loanform.setvalue('对手性别', '') # 属性隐藏
        # loanform.setvalue('机构分类', '产险公司') # 属性隐藏
        # loanform.setvalue('出生日期', '') # 属性隐藏
        loanform.setvalue('组织机构代码', '1000397')
        loanform.setvalue('社会信用代码', '1000397')
        loanform.setvalue('贷款卡号', '1000397')
        # loanform.setvalue('证件类型', '') # 属性隐藏
        # loanform.setvalue('证件号码', '') # 属性隐藏
        loanform.setvalue('企业特征', '大型企业')
        loanform.setvalue('企业性质', '企业法人(公司、非公司制企业法人)')
        loanform.setvalue('行业分类', '基础产业')
        loanform.setvalue('明细分类', '农业(大类)')
        # loanform.setvalue('职业分类', '政府部门') # 属性隐藏
        loanform.setvalue('归属国别', 'CHN:中华人民共和国')
        loanform.setvalue('对手方子类', '银行类')
        loanform.setvalue('内部评级', 'AAA')
        loanform.setvalue('外部评级', 'AAA')
        #loanform.setvalue('外部评级机构', '请选择')
        loanform.setvalue('公司类型', '内资企业')
        loanform.setvalue('注册类型', '工商注册号')
        loanform.setvalue('登记注册号', '1000397')
        loanform.setvalue('注册资本', '元')
        loanform.setvalue('企业法人', '1000397')
        loanform.setvalue('法人证件类型', '护照')
        loanform.setvalue('法人证件代码', '1000397')
        loanform.setvalue('企业成立日期', '20170821')
        loanform.setvalue('登记开始日期', '20170821')
        loanform.setvalue('登记到期日期', '20170821')
        loanform.setvalue('国税登记证号', '1000397')
        loanform.setvalue('地税登记证号', '1000397')
        loanform.setvalue('是否上市', '是')
        loanform.setvalue('上市地', '上海')
        loanform.setvalue('股票代码', '1000397')
        loanform.setvalue('是否集团', '是')
        loanform.setvalue('经营类型', '联营企业')
        loanform.setvalue('合作类型', '共管公司')
        loanform.setvalue('关联类型', '无')
        #loanform.setvalue('所属集团', '请选择')
        loanform.setvalue('综合评级', 'AAA')
        loanform.setvalue('资本金(元)', '1,000,397.00')
        loanform.setvalue('总资产', '1000397')
        loanform.setvalue('净资产', '1000397')
        loanform.setvalue('通讯地址', '1000397')
        loanform.setvalue('联系人', 'webUI')
        loanform.setvalue('财务部电话', '1000397')
        loanform.setvalue('电话', '1000397')
        loanform.setvalue('传真', '1000397')
        loanform.setvalue('邮编', '410082')
        loanform.setvalue('邮箱', '1000397@qq.com')
        return
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
        b = driver.getelementbyattribute(r'css selector:.hc_selectbox-tree-div,style:[\s\S]*display: block;[\s\S]*')
       
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
    #beginform = driver.getallframe(driver.driver)
    role1 =loanrival(driver)
    #role1.search()
    role1.add()
    #role1.add()
    #role1.modify()
    #role1.delete()
    #role1.rolemanageadd()
    #role1.delete()
    
    #role1.end()