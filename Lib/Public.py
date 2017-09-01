'''
Created on 2017楠烇拷8閺堬拷1閺冿拷

@author: niucx14840
'''



import Lib.ClassSelenium as ClassSelenium
from Lib.ClassSelenium import ElementObject
import time
from warnings import catch_warnings
from _ast import Num
import re


# addwin=driver.getelementbyattribute(r'xpath://child::div[@style="display: block;"]/div[2]')
#  b = driver.getelementbyattribute('css selector:.hc_selectbox-tree-div,display:block')
#  css selector:.hc_selectbox-tree-div,style:[\s\S]*display: block;
# xpath:descendant::label[@title="{0}"]/following-sibling::*/descendant::*/input[@title]'.format(value)

def switchlabeldriver(driver:ClassSelenium,label:str):
    driver.driver.switch_to_default_content()

    driver.switchtoframe()

def exceptioncheck(windriver):
    try:
        windriver.getelementbyattribute(r'css selector:.verify-tip-inner',getall = True)
    except Exception as ex:
        pass
    else:
        raise ClassSelenium.SeleniumError("css.verify-tip-inner:"+"输入值有误")

def getheaderlist():
    #tableheader = driver._findelementbyattribute(r'css selector', '.hc-datagrid-header','',None) #瀹氫箟琛ㄦ牸鎶�
    tableheader=driver.getelementbyattribute('css selector:.hc-datagrid-header') 
    tablebody = driver.getelementbyattribute('css selector:.hc-datagrid-body') #鑾峰彇琛ㄦ牸浣�
    headerlist = dict()
    templist = tableheader.getelementbyattribute('css selector:table>tbody>tr>td',getall = True)

    num = 0
    for temp in templist:
        if num == 0:
            headerlist['序号'] = 0
        elif num ==1:
            headerlist['选框'] = 1
        else:
            name = temp.getelementbyattribute(r"tag name:div",getall = True)[0].gettext()
            headerlist[name] = num
            
        num +=1
    
    
    temptrbody = tablebody.getelementbyattribute('css selector:table>tbody>tr', getall =True)
    bodylist = []
    for rowbody in  temptrbody:
        temptdbodys = rowbody.getelementbyattribute('css selector:td>div',getall=True)
        thtextlist = [x.gettext() for x in temptdbodys ]
        bodylist.append(thtextlist)
    return headerlist,bodylist
        #for temptdbody in temptdbody:
         #   thtextlist = []
         #   thtextlist.append(temp)
        
def SelectListData(driver,k,v):
    '''k:列名  v:cell值��
    '''
    i=1
    j=1
    elements=None
    try:
        elements=driver.getelementbyattribute('css selector:.hc-datagrid-header>table>tbody>tr>td',getall = True)
    except:
        elements = driver.getelementbyattribute('css selector:.hc-datagrid-body>table>thead>tr>td', getall=True)

    for m in elements:
        xt = m.gettext()  # 获取表头值�
        if xt == k:
            break
        i = i + 1
    
    element1s=driver.getelementbyattribute('css selector:.hc-datagrid-body>table>tbody>tr',getall=True)
    for n in  element1s:
        ts=n.getelementbyattribute('css selector:td:nth-child('+str(i)+')',getall = True)
        xs=ts[0].gettext()   # 获取cell值�
        
        if xs==v:
            ts[0].Click()
            break
        j=j+1



def readonly(*kw):

    for i in kw:
        if not i.getattribute('readonly'):
            return False
    return True

def notemptycheck(*kw):
    for i in kw:
        if i.gettext() == ''or i.gettext()== None or i.getattribute('title') :
            return False
        else:
            return True
     
def htips(driver,value):
    '''
    driver传入driver
    value传tips提示值，如果一直返回true，不一致返回false
    '''
    htip = driver.getelementbyattribute(r"xpath://div[@class='h_tips']").gettext();
    return(value in htip)

def msgfloat(driver,vtile,vbody,action,error='操作失败'):
    '''
    vtite:弹出标题
    vbody:弹出窗提示文本
    action：传入按钮文本 
    error：抛异常文本信息
    '''
    h_msg_floatdiv = driver.getelementbyattribute('id:h_msg_floatdiv',getall=True)[0]
    title = h_msg_floatdiv.getelementbyattribute('css selector:.m-message-header').gettext()
    body = h_msg_floatdiv.getelementbyattribute('css selector:.m-body-words').gettext()
    footer = h_msg_floatdiv.getelementbyattribute('css selector:.h_btndiv.m-message-footer').gettext()
    if title !=vtile or (vbody not in body):
        raise ClassSelenium.SeleniumError(error+"失败，原因:"+body)
    h_msg_floatdiv.getelementbyattribute('tag name:button,text:'+action).Click()

class form(object):
    def __init__(self,driver,window:ElementObject):
        self.driver = driver
        self.window = window
        if not isinstance(window,ElementObject):
            self.loanform = window.getelementbyattribute('tag name:form',getall=True)[0]
        elif window.gettagname() =='form':
            self.loanform=window
        else:
            self.loanform = window.getelementbyattribute('tag name:form',getall=True)[0]
        self.hidediv = driver.getelementbyattribute('id:hc_hide_div')

    def __getitem__(self, value):
        self._getinput(value)
        return self.curinputele
    def _getinput(self,name):
#         tempstr = 'xpath:descendant::label[@title="{0}"]/following-sibling::*/descendant::*/input[@title]'.format(value)
        tempstr = 'xpath:descendant::label[@title="{0}"]/following-sibling::*/descendant::*/input'.format(name)
        inputlist = self.loanform.getelementbyattribute(tempstr,getall='True')

        if(len(inputlist) == 1):
            self.curinputele = inputlist[0]
        elif(len(inputlist) == 2):
            self.curinputele = inputlist[1]
        elif(len(inputlist) == 3):
            self.curinputele = inputlist[1]
        else:
            raise ClassSelenium.SeleniumExceptions("Form有新的输入框类型出现，需要添加功能")
        return self.curinputele
    def _geteletype(self):

        # 获取输入框的class属性，根据css属性不同判断输入框的类型
        tempcss = self.curinputele.getattribute('class')

        if 'u-textfield' in tempcss :
            return 'str'
        elif  'u-select' in tempcss:
            if 'hc_select-tree' in tempcss:
                return 'singtree'
            elif  'combox_disabled' in tempcss:
                return  'combox'
#             elif self.curinputele.getattribute('multiple') == 'true':
#                 return 'mulselect'
            else:
                return 'select'
        elif 'u-calendar' in tempcss :
            return 'calendar'
    def _settextvalue(self,value):
        self.curinputele.clear()
        self.curinputele.Click()
        self.curinputele.sendkeys(value)
        #title = self.curinputele.getattribute('value title')
        # if title != value:
        #     raise ClassSelenium.SeleniumExceptions('文本控件输入值:{0} 不成功'.format(value))
    def _setselevalue(self,value):
        self.curinputele.Click()
        #temp = self.hidediv.getelementbyattribute('tag name:div,style:[\s\S]*display: block;[\s\S]*')
        temp = self.driver.getelementbyattribute('xpath:.//div[@id="hc_hide_div"]/div,style:[\s\S]*display: block;[\s\S]*')
        if  temp.getattribute('multiple_line') == 'true':   # 如果是多选框执行多选框赋值函数
            self._setmulselevalue(value)
        else:
            #tempstr = 'xpath:ul/li[@title ="{0}"]'.format(value)
            value=value.strip()
            tempstr = 'xpath:ul/li/label,text:\s*{0}\s*'.format(value)
            listele = temp.getelementbyattribute(tempstr)
            listele.Click()
            title = self.curinputele.getattribute('title').strip()
            if title!=value:
                raise ClassSelenium.SeleniumExceptions('单选框值:{0} 选择不成功'.format(value))
    def _setmulselevalue(self,value):
        '''
            value:支持多个值传入，用','隔开
        '''
        #self.curinputele.Click()
        #temp = self.hidediv.getelementbyattribute('tag name:div,style:[\s\S]*display: block;[\s\S]*')
        temp = self.driver.getelementbyattribute('xpath:.//div[@id="hc_hide_div"]/div,style:[\s\S]*display: block;[\s\S]*')
        # 已经选择的全部清除
        try:
            listeles = temp.getelementbyattribute('xpath:ul/li[@class="h_cur"]',getall=True)
            for i in listeles:
                i.Click()
        except Exception as e:
            print("except",e)
        #values = set(value.split(','))
        for i in value:
            #tempsrt = 'xpath:ul/li,title:\s*{0}\s*'.format(i)
            tempstr = 'xpath:ul/li/label,text:\s*{0}\s*'.format(value)
            listele = temp.getelementbyattribute(tempsrt)
            listele.Click()
        title = self.curinputele.getattribute('title')
        if len(title.split(',')) != len(value):
            raise ClassSelenium.SeleniumExceptions('多选框值:{0} 选择不成功'.format(value))
        self.loanform.Click()
    def _setcalendarvalue(self,value):
        self.curinputele.Click()
        self.curinputele.clear()
        xpathstr = 'xpath://div[@class="h_screen"]/following-sibling::div,style:[\s\S]*display: block;[\s\S]*,class:[\s\S]*datetimepicker[\s\S]*'
        temp = self.driver.getelementbyattribute(xpathstr)
        self.curinputele.sendkeys(value)
        self.curinputele.Click()
        temp.getelementbyattribute('css selector:.day.active').Click()
        inputdate = self.curinputele.getelementbyattribute('xpath:preceding-sibling::input',getall =True)[0]
        title = inputdate.getattribute('value')
        if title != value:
            raise ClassSelenium.SeleniumExceptions('文本控件输入值:{0} 不成功'.format(value))
        self.loanform.Click()
    def _setsingtreevalue(self,value):
        self.curinputele.Click()
        self.curinputele.sendkeys(value[:1])
        #temp = self.hidediv.getelementbyattribute('tag name:div,style:[\s\S]*display: block;[\s\S]*')
        temp =  self.driver.getelementbyattribute('xpath://div[@class="h_screen"]/following-sibling::div/div[1],style:[\s\S]*display: block;')
        listele = self.driver.getelementbyattribute(r'xpath:.//span[text()="{0}"]'.format(value))
        listele.Click()
        title = self.curinputele.getattribute('title')
        if title!=value:
            raise ClassSelenium.SeleniumExceptions('单选属性选择控件选择值:{0} 不成功'.format(value))

    def setvalue(self,name,value):
        
        try:
            hand = self.loanform.getelementbyattribute('xpath:descendant::label[@title="{0}"]/following-sibling::div/div/i[@class="fa fa-hand-pointer-o u-autoitem-down"]'.format(name))
        except:
            pass
        else:
            hand.Click()
            tempaddwin = self.driver.getelementbyattribute(r'xpath://body/div[@style="display: block;"][last()]/div[2]')
            handobject = choosehand(self.driver,tempaddwin)
            handobject.fastserach(value)
            return

        self._getinput(name)
        cureletype = self._geteletype()
        if cureletype=='str':
            self._settextvalue(value)
        elif cureletype=='calendar':
            self._setcalendarvalue(value)
        elif cureletype=='singtree':
            self._setsingtreevalue(value)
        elif cureletype=='select':
            self._setselevalue(value)
    def printlabel(self):
        x = input("请在Form输入值，按任意键继续")

        labellist = self.loanform.getelementbyattribute('xpath:descendant::label[@title]',getall ='True') # 获取表单的所有输入框
        for i in labellist:
            try:
                if i.is_displayed():
                    lable = i.getattribute('title').strip(r'*').strip()

                    title = self._getinput(lable).getattribute('title')

                    print("loanform.setvalue('{0}', '{1}')".format(lable,title))
                else:
                    lable = i.getattribute('title').strip(r'*').strip()
                    title = self._getinput(lable).getattribute('title')
                    print("#loanform.setvalue('{0}', '{1}') # 属性隐藏".format(lable, title))
            except Exception as e:
                print(lable,e)
                print("#loanform.setvalue('{0}') # {1}".format(lable,e))
    def button(self,name):
        exceptioncheck(self.window)
        self.window.getelementbyattribute('tag name:button,text:{0}'.format(name)).Click()
        exceptioncheck(self.window)

class chooseloanrival(object):
    def __init__(self,driver,window:ElementObject):
        self.driver = driver
        self.window = window
        self.sform = form(driver,window)

    def search(self,l_rival_id=None,vc_all_name=None,vc_rival_type=None):
        """
        通过输入条件,查询对手方，如果不输入默认为None
        :param l_rival_id: 对手方序号
        :param vc_all_name: 对手方名称
        :param vc_rival_type: 对手方类型
        :return: 空
        """
        if l_rival_id:
            self.sform.setvalue('对手序号',l_rival_id)
        if vc_all_name:
            self.sform.setvalue('对手方名称 ',vc_all_name)
        if vc_rival_type:
            self.sform.setvalue('对手类型',vc_rival_type)
        self.sform.button('查询')
    def fastserach(self,l_rival_id=None,vc_all_name=None,vc_rival_type=None):
        """
        这个函数包括搜索选择点击查询一套流程，要求l_rival_id必须有效
        :param l_rival_id:
        :param vc_all_name:
        :param vc_rival_type:
        :return:
        """
        self.search(l_rival_id,vc_all_name,vc_rival_type)
        self.choosedata('对手序号',l_rival_id)
        self.button('选择')
    def choosedata(self,title,value):
        """
        通过搜索表单对应列名以及那一列包含单的单元格值获取要选择的行，然后选定这一行
        :param title: 表单列名
        :param value: 表单列名那一列选择的值
        :return: 空
        """
        SelectListData(self.window,title,value)
    def button(self,name):
        self.window.getelementbyattribute('tag name:button,text:选择').Click()
        if self.window.is_displayed():
            raise ClassSelenium.SeleniumExceptions('对手方选择框没有正常关闭')

class choosehand(object):
    def __init__(self,driver,window:ElementObject):
        self.driver = driver
        self.window = window
        self.sform = form(driver,window)
        self.names = []
        labels = self.window.getelementbyattribute('xpath:descendant::label[@title]', getall=True)
        for label in labels:
            if  label.is_displayed:
                self.names.append(label.getattribute('title'))
    def search(self,*kw,**kkw):
        """
        通过输入条件,查询对手方，如果不输入默认为None
        :param l_rival_id: 对手方序号
        :param vc_all_name: 对手方名称
        :param vc_rival_type: 对手方类型
        :return: 空
        """
        if kw:
            if len(self.names)<len(kw):
                raise ClassSelenium.SeleniumExceptions('输入框和参数数值对应不正确')
            i = 0
            for j in kw:
                self.sform.setvalue(self.names[0],j)
                i +=1

        elif kkw:
            for (name,value) in kkw.items():
                self.sform.setvalue(name,value)
        self.sform.button('查询')
    def fastserach(self,*kw,**kkw):
        """
        这个函数包括搜索选择点击查询一套流程，要求l_rival_id必须有效
        :param l_rival_id:
        :param vc_all_name:
        :param vc_rival_type:
        :return:
        """
        self.search(*kw,**kkw)
        self.choosedata(*kw,**kkw)
        self.button('选择')
    def choosedata(self,*kw,**kkw):
        """
        通过搜索表单对应列名以及那一列包含单的单元格值获取要选择的行，然后选定这一行
        :param title: 表单列名
        :param value: 表单列名那一列选择的值
        :return: 空
        """
        if kw:
            SelectListData(self.window,self.names[0],kw[0])
        if kkw:
            SelectListData(self.window, self.names[0],kw[self.names[0]])
    def button(self,name):
        self.window.getelementbyattribute('tag name:button,text:选择').Click()
        if self.window.is_displayed():
            raise ClassSelenium.SeleniumExceptions('对手方选择框没有正常关闭')
def setvalue(inputform:form,dic:dict,begin:str,end:str):
    flag = False
    for (key,value) in dic.items():
        #print(key, value)
        name = key.split('_')[0]
        if key==begin or flag :
            flag =True
            if value:
                if '=' in value:
                    tempdict = {}
                    temps = value.spit(',')
                    for temp in temps:
                        tempdict[temp.split('=')[0]]=temp.split('=')[1]
                        inputform.setvalue(name,tempdict)
                elif ',' in value:
                    inputform.setvalue(name, value.split(','))
                #print('inputform.setvalue({0},{1})'.format(key,value))
                else:
                    inputform.setvalue(name,value)
        if key == end:
            return


if __name__ == '__main__':
    global driver
    driver=ClassSelenium.ClassSelenium("http://10.20.25.124:8080/am/login.htm,chrome")
    driver.getelementbyattribute("id:vc_op_code").sendkeys('8888')
    driver.getelementbyattribute('id:vc_op_password').sendkeys("123456")   #��
    driver.getelementbyattribute('id:login').Click()
    driver.getelementbyattribute('link text:系统管理').Click()#菜单
    driver.getelementbyattribute('link text:系统配置管理').Click()#菜单
    driver.getelementbyattribute('xpath:ul[style=display: block;]/li[@title={0}]'.format('dbf上传配置管理')).Click()#菜单
    #閼惧嘲褰囬悽銊﹀煕鐞涖劌宕�
    global operatable
#     operatable=driver.getelementbyattribute('tag name:table,id:data_table_dataTable')
    #閼惧嘲褰囬悽銊﹀煕閸旂喕鍏橀懣婊冨礋
    global buttonmenu

    SelectListData(driver,'用户名','1212')

    pass