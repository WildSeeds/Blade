#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions as SeleniumExceptions
import time
import re
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from Lib.Common import toolfolderpath,flag
class ClassSelenium():
    '''
    classdocs
    '''
    def __init__(self, params):
        self.mythread=None
        self.mythreadname=None
        try:
            #使用，分割，获取浏览器类型
            temp=params.replace('，',',').split(',')
            url=temp[0]
            try:
                browsertype=temp[1].lower()
            except IndexError:
                browsertype=r'firefox'
            if browsertype==r'firefox':
                self.driver=webdriver.Firefox()
            else:
                #获取当前系统是32位还是64位
                import platform
                osbit=platform.architecture()[0]
                if browsertype==r'ie':
                    self.mythreadname=r'IEDriverServer.exe'
                    if osbit=='64bit':
                        exepath=toolfolderpath+r'IEDriverServer_x64'+flag+r'IEDriverServer.exe'
                    else:
                        exepath=toolfolderpath+r'IEDriverServer_win32'+flag+r'IEDriverServer.exe'
                elif browsertype==r'chrome':
                    self.mythreadname=r'chromedriver.exe'
                    exepath=toolfolderpath+r'chromedriver'+flag+r'chromedriver.exe'
                else:
                    print('请确认初始化表格中，浏览器类型是否书写正确，目前只支持：ie、firefox和chrome')
                    raise Exception
                webdriver_driver = os.path.abspath(exepath)
                os.environ["webdriver.driver"] = webdriver_driver
                if browsertype==r'ie':
                    self.driver = webdriver.Ie(webdriver_driver)
                elif browsertype==r'chrome':
                    options = webdriver.ChromeOptions()
                    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
                    self.driver = webdriver.Chrome(webdriver_driver,chrome_options=options)
            self.driver.get(url)
            self.driver.maximize_window()
        except Exception as aa:
            print(aa)
    
    def classtype(self):
        return r'ui'
    
    def switchtoframe(self,framename=None):
        if isinstance(framename, str) or isinstance(framename, int):
            self.driver.switch_to_frame(framename)
        elif isinstance(framename, ElementObject):
            self.driver.switch_to_frame(framename.changetoWebElement())
        else:
            self.driver.switch_to_default_content()
    
    def getalerttext(self,alertoper='accept'):
        """
        alertoper：对当前文本框的操作，accept为确定，dismiss为取消
                            获取弹出框的文本内容并返回
        """
        alert=self.driver.switch_to_alert()
        alerttext=alert.text
        if alertoper=='dismiss':
            alert.dismiss()
        else:
            alert.accept()
        return alerttext
    
    def closecurrwindow(self):
        '''
        closecurrwindow:关闭当前网页窗口
        '''
        self.driver.close()
    
    def switchtowindow(self,title_name,timeout=10):
        """
        switchtowindow:切换当前浏览器中的不同标签页，直到找到指定的标题名的标签页
        """
        curr_time=0
        while curr_time<timeout:
            all_handles = self.driver.window_handles
            for handle in all_handles:
                self.driver.switch_to_window(handle)
                curr_title_name=self.driver.title
                if curr_title_name.strip()==title_name.strip():
                    return
            time.sleep(1)
            curr_time+=1
        print("没有找到title为"+title_name+"的网页，请确认!")
        raise SeleniumError("没有找到title为"+title_name+"的网页，请确认!")
    
    def _focus_elementobject(self,ElementObject):
        self.driver.execute_script("arguments[0].scrollIntoView();", ElementObject)
        
    def drop_up_scroll(self,X_position=0,Y_position=0):
        '''
        drop_up_scroll:操作滚动条函数,默认恢复到最初始,目前是适用火狐和IE浏览器
        X_position:相对左上角的横坐标偏离位置，操作横向滚动条的参数
        Y_position:相对左上角的纵坐标偏离位置，操作纵向滚动条的参数
        '''
        self.driver.execute_script("window.scrollTo({0}, {1})".format(X_position,Y_position))
    
    def doubleclick(self, ElementObject):
        ActionChains(self.driver).double_click(ElementObject.changetoWebElement()).perform()
        
    def leftclick(self, ElementObject):
        ActionChains(self.driver).click(ElementObject.changetoWebElement()).perform()
        
    def rigthclick(self, ElementObject):
        ActionChains(self.driver).context_click(ElementObject.changetoWebElement()).perform()
        
    def movetoelement(self, ElementObject):
        ActionChains(self.driver).move_to_element(ElementObject.changetoWebElement()).perform()
    
    def close(self):
        """
                            关闭对象,固有函数，不可删除
        """
        self.driver.quit()
    
        
    def getallframe(self,ele):
        """
        alertoper：对当前文本框的操作，accept为确定，dismiss为取消
                            获取弹出框的文本内容并返回
        """
        framelist=ele.find_elements("tag name", "frame")
        iframelist=ele.find_elements("tag name", "iframe")
        framelist.extend(iframelist)
        templist=[ElementObject(self,x) for x in framelist]
        return templist
    
    def exist(self,attrdes,timeout=None):
        """
        attrdes:为对象，其中主属性必须包含id,xpath,link text,partial link text,name,tag name,class name,css selector其中一个或多个
                            其他辅助属性，为type,value，辅助属性支持正则
        timeout:超时时间，默认为20秒
        """
        try:
            if timeout:
                findresult=self.getelementbyattribute(attrdes,TIMEOUT=timeout)
            else:
                findresult=self.getelementbyattribute(attrdes)
        except SeleniumError:
            findresult=None
        return findresult
    
    def isdisplayed(self,attrdes):
        """
        attrdes:为对象，其中主属性必须包含id,xpath,link text,partial link text,name,tag name,class name,css selector其中一个或多个
                            其他辅助属性，为type,value，辅助属性支持正则
        """
        try:
            findresult=self.getelementbyattribute(attrdes)
        except noisplayError:
            return False
        return findresult
    
    def getelementbyattribute(self,attrdes,getall=None,farther=None,TIMEOUT=20):
        timecount=0
        elements=None
        primary=False
        if not farther:
            farther=self.driver
        #检测当前字符串是否有主属性,由于是部分匹配，所以列表中顺序不可变
        attrlist=['tag name','partial link text','link text','class name','id','name','css selector','xpath']
        #从属性字符串中找出主属性，优先找出tag name
        for attrstr in attrlist:
            if re.search(attrstr+':[^,]*',attrdes):
                primary=re.search(attrstr+':[^,]*', attrdes).group()
                assist=attrdes.replace(primary,'').strip(',')
                #assist=re.sub(primary+':[^,]*', '', attrdes).strip(',')
                break
        #分解主属性，获取主属性和值
        if not primary:
            print(attrdes+"中没有找到主属性，请确认!")
            raise SeleniumError(attrdes+"中没有找到主属性，请确认!")
        primaryindex=primary.index(":")
        #self.switchtoframe()
        while timecount<TIMEOUT:
            elements=self._findelementbyattribute(primary[0:primaryindex], primary[primaryindex+1:],assist,farther)
            if  not elements:
                timecount+=1
            else:
                break
        if not elements:
            print(attrdes+"属性对象没有找到!")
            raise SeleniumError(attrdes+"属性对象没有找到!")
        if getall:
            templist=[ElementObject(self,x) for x in elements]
            return templist
        else:
            lennumber=len(elements)
            if lennumber==1:
                timecount=1
                while (not elements[0].is_displayed()) and timecount<TIMEOUT:
                    time.sleep(1)
                    timecount+=1
                if elements[0].is_displayed():
                    return ElementObject(self,elements[0])
                else:
                    print(attrdes+"属性对象不可以操作，请确认!")
                    raise noisplayError(attrdes+"属性对象不可以操作，请确认!")
            elif lennumber>0:
                print(attrdes+"属性对象找到多个，请确认!")
                raise SeleniumError(attrdes+"属性对象找到多个，请确认!")
        
    def _findelementbyattribute(self,key,value,assist,farther=None):
        """
        attrdes:为对象，其中主属性必须包含id,xpath,link text,partial link text,name,tag name,class name,css selector其中一个或多个
                            其他辅助属性，为type,value，辅助属性支持正则
        getall:返回对象集合，默认为返回单个元素
        farther:父节点对象，默认为ClassSelenium中driver对象，即整个浏览器
        TIMEOUT:设置超时时间
                            所有对象属性书写方式为,"attr:value"，多个属性使用,分割，如果最后对象总数为1则返回对象，大于1则返回错误提示根据属性找到大于1的对象，提示增加辅助属性
                            如果没有找到，则会再次查找，超过超时时间后，如果还是没有找到，则报无对象错误，默认超时时间为20秒
        """
        elements=None
        findException=True
        if not farther:
            farther=self.driver
        while(findException):
            try:
                elements=farther.find_elements(key, value)
                break
            #增加异常StaleElementReferenceException抓捕，防止出现对象刷新导致的对象获取失效
            except SeleniumExceptions.StaleElementReferenceException:
                time.sleep(1)
            except Exception as e:
                print(e)
        if elements and assist:
            #根据辅助属性，找出筛检对象
            assistlist=assist.split(sep=",")
            for e in assistlist:
                indexnumber=e.index(":")
                i=0
                #从主属性对象集合中找出附属属性
                while i<len(elements):
                    if e[0:indexnumber]=='text':
                        re_str='^'+e[indexnumber+1:]+'$'
                        if e[indexnumber+1:].startswith('.'):
                            re_str=re_str.strip('^')
                        if e[indexnumber+1:].endswith('.*'):
                            re_str=re_str.strip('$')
                        if not re.search(re_str,elements[i].text.strip()):
                            elements.remove(elements[i])
                        else:
                            i+=1
                    else:
                        #正则表达式中需要做设定，必须以给定的字符串打头和结尾
                        #print(e[0:indexnumber],'^'+e[indexnumber+1:]+'$',elements[i].get_attribute(e[0:indexnumber]))
                        if not (elements[i].get_attribute(e[0:indexnumber]) and re.search('^'+e[indexnumber+1:]+'$',elements[i].get_attribute(e[0:indexnumber]))):
                            elements.remove(elements[i])
                        else:
                            i+=1
        if not elements:
            framelist=self.getallframe(farther)
            for eachframe in framelist:
                try:
                    self.switchtoframe(eachframe)
                except SeleniumExceptions.WebDriverException:
                    break
                elements=self._findelementbyattribute(key,value,assist,farther)
                if not elements:
                    self.driver.switch_to.parent_frame()
        return elements            
        
    
class ElementObject(ClassSelenium):
    
    def __init__(self,driver,EO):
        self.eleobject=EO
        self.id=EO.id
        self.parent = EO._parent
        self.w3c = EO._w3c
        self.driver=driver
        
    def sendkeys(self,inputstr):
        self.eleobject.send_keys(inputstr)
    
    def keyboard(self,inputstr):
        """
        keyboard:模拟键盘操作，只支持如下参数输入
        keyboardNULL,CANCEL,HELP,BACKSPACE,BACK_SPACE,TAB,CLEAR,RETURN,ENTER,SHIFT,LEFT_SHIFT,CONTROL,LEFT_CONTROL,ALT,LEFT_ALT,PAUSE,ESCAPE,SPACE
        PAGE_UP,PAGE_DOWN,END,HOME,LEFT,ARROW_LEFT,UP,ARROW_UP,RIGHT,ARROW_RIGHT,DOWN,ARROW_DOWN,INSERT,DELETE,SEMICOLON,EQUALS,NUMPAD0
        NUMPAD1,NUMPAD2,NUMPAD3,NUMPAD4,NUMPAD5,NUMPAD6,NUMPAD7,NUMPAD8,NUMPAD9,MULTIPLY,ADD,SEPARATOR,SUBTRACT,DECIMAL,DIVIDE,
        F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,META,COMMAND
        """
        self.eleobject.send_keys(eval('Keys.'+inputstr))
    
    def getattribute(self,inputstr):
        return self.eleobject.get_attribute(inputstr)
    
    def isreadonly(self):
        """
        attrdes:为对象，其中主属性必须包含id,xpath,link text,partial link text,name,tag name,class name,css selector其中一个或多个
                            其他辅助属性，为type,value，辅助属性支持正则
        """
        findresult=self.getattribute('readonly')
        if findresult==None:
            return False
        else:
            return True
    
    def _focus_element(self):
        ClassSelenium._focus_elementobject(self.driver,self.eleobject)
    
    def Click(self):
        try:
            self.eleobject.click()
        except Exception as aa:
            #处理可能出现的元素不在界面显示，无法点击的问题，将使用滚动条切换到可显示指定元素的位置，然后再做一次点击操作
            Exception_str='{0}'.format(aa)
            if 'Element is not clickable at point' in Exception_str:
                self._focus_element()
                self.eleobject.click()
            else:
                raise aa
    
    def gettabletitle(self):
        """
        gettabletitle:获取table对象的title属性，以列表的形式返回
        """
        if self.gettagname()=='table':
            titlestr=self.getelementbyattribute(r'tag name:thead').gettext()
            titlelist=re.findall(r'[^\n]+',titlestr)
            return titlelist
        else:
            print('元素对象不为table对象，对象类型为：'+self.gettagname())
            raise SeleniumError('元素对象不为table对象，对象类型为：'+self.gettagname())
        
    def gettabletext(self):
        """
        gettabletitle:获取table对象的title属性，以列表的形式返回
        """
        if self.gettagname()=='table':
            bodystr=self.getelementbyattribute(r'tag name:tbody').gettext()
            bodylist=re.findall(r'[^\n]+',bodystr)
            return bodylist
        else:
            print('元素对象不为table对象，对象类型为：'+self.gettagname())
            raise SeleniumError('元素对象不为table对象，对象类型为：'+self.gettagname())
        
    def gettablecellbytitleandrow(self,titlename,rownumber):
        """
        gettablecellbytitleandrow:根据列名和行数获取单元格元素对象
        titlename:标题名字
        rownumber:行数
        """
        if self.gettagname()=='table':
            titlenames=[]
            #需要判断第一个是否为无标题全选框
            titleelements=self.getelementbyattribute(r'tag name:thead').getelementbyattribute('tag name:tr').getelementbyattribute(r'tag name:th', True)
            for each in titleelements:
                if each.gettext():
                    titlenames.append(each.gettext())
                else:
                    #如果不存在text属性，则以name属性代替
                    titlenames.append(each.getelementbyattribute('tag name:input').getattribute('name'))
            #找出当前title在titles中的列数
            titleindex=titlenames.index(titlename)
            tabletextelements=self.getelementbyattribute(r'tag name:tbody').getelementbyattribute('tag name:tr', True)
            tablerowelement=tabletextelements[rownumber-1]
            tablecellelements=tablerowelement.getelementbyattribute(r'tag name:td', True)
            tablecellelement=tablecellelements[titleindex]
            return tablecellelement
        else:
            print('元素对象不为table对象，对象类型为：'+self.gettagname())
            raise SeleniumError('元素对象不为table对象，对象类型为：'+self.gettagname())
    def gettablecellbytitleandvalue(self,titlename,value):
        """
        gettablecellbytitleandrow:根据列名和行数获取单元格元素对象
        titlename:标题名字
        rownumber:行数
        """
        if self.gettagname()!='table':
            self = self.getelementbyattribute('tag name:table')
        
        titlenames=[]
        #需要判断第一个是否为无标题全选框
        titleelements=self.getelementbyattribute(r'tag name:thead').getelementbyattribute('tag name:tr').getelementbyattribute(r'tag name:td', True)
        for each in titleelements:
#             if each.gettext():
#                 titlenames.append(each.gettext())
#             else:
#                 #如果不存在text属性，则以name属性代替
#                 titlenames.append(each.getelementbyattribute('tag name:input').getattribute('name'))
            titlenames.append(each.gettext())
        #找出当前title在titles中的列数
        titleindex=titlenames.index(titlename)
        tabletextelements=self.getelementbyattribute(r'tag name:tbody').getelementbyattribute('tag name:tr', True)
        for tablerowelement in tabletextelements:
            #tablerowelement=tabletextelements[rownumber-1]
            tablecellelements=tablerowelement.getelementbyattribute(r'tag name:td', True)
            tablecellelement=tablecellelements[titleindex]
            if tablecellelement.gettext() == value:
                tablecellelement.Click()
                return tablecellelement
        raise SeleniumError('未找到列:'+titlename+'值'+value)
            

 
    def getrowbytitleandtext(self,titlename,text):
        """
        getrowbytitleandrow:获取指定文本在表格中第一次出现的行数
        titlename:标题名字
        text:需要查找的文本
        """
        if self.gettagname()=='table':
            titlenames=[]
            row=1
            #需要判断第一个是否为无标题全选框
            titleelements=self.getelementbyattribute(r'tag name:thead').getelementbyattribute('tag name:tr').getelementbyattribute(r'tag name:th', True)
            for each in titleelements:
                if each.gettext():
                    titlenames.append(each.gettext())
                else:
                    #如果不存在text属性，则以name属性代替
                    titlenames.append(each.getelementbyattribute('tag name:input').getattribute('name'))
            #找出当前title在titles中的列数
            titleindex=titlenames.index(titlename)
            tabletextelements=self.getelementbyattribute(r'tag name:tbody').getelementbyattribute('tag name:tr', True)
            #逐条寻找指定文本
            for each in tabletextelements:
                tablecellelements=each.getelementbyattribute(r'tag name:td', True)
                tablecellelement=tablecellelements[titleindex]
                if tablecellelement.gettext()==text:
                    return row
                else:
                    row+=1
            print('在table中的'+titlename+'列下没有找到'+text+'内容单元格')
            raise SeleniumError('在table中的'+titlename+'列下没有找到'+text+'内容单元格')
        else:
            print('元素对象不为table对象，对象类型为：'+self.gettagname())
            raise SeleniumError('元素对象不为table对象，对象类型为：'+self.gettagname())
    
    def getelementbyattribute(self,attrdes, getall=None):
        return ClassSelenium.getelementbyattribute(self, attrdes, getall,self.eleobject)
    
    def gettext(self):
        return self.eleobject.text
    
    def isenabled(self):
        return self.eleobject.is_enabled()
    
    def gettagname(self):
        return self.eleobject.tag_name
    
    def changetoWebElement(self):
        return WebElement(self.parent,self.id,self.w3c)
    
    def clear(self):
        self.eleobject.clear()
    
    def select(self,value):
        """
        select:对下拉框对象进行选取操作
        value:下拉框的值
        """
        if self.gettagname()=='select':
            #需要判断第一个是否为无标题全选框
            titleelements=self.getelementbyattribute(r'tag name:option', True)
            for each in titleelements:
                if each.gettext()==value:
                    each.Click()
                    return 'pass'
            print('在下拉框中下没有找到'+value+'选项')
            raise SeleniumError('在下拉框中下没有找到'+value+'选项')
        else:
            print('元素对象不为下拉框对象，对象类型为：'+self.gettagname())
            raise SeleniumError('元素对象不为下拉框对象，对象类型为：'+self.gettagname())
        """
        from selenium.webdriver.support.select import Select
        Select(self.eleobject).select_by_value(value)
        """
    def is_displayed(self):
        return self.eleobject.is_displayed()
class SeleniumError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
class noisplayError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

if __name__ == '__main__':
    abc=ClassSelenium("http://www.baidu.com/,ie")
    time.sleep(2)

    #abc.getelementbyattribute('id:username_id').changetoWebElement().send_keys(r'hundsun')
    #abc.getelementbyattribute('id:password_id').sendkeys(r'hundsun')
    