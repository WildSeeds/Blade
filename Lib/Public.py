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
global driver
global InputData
global UIExcept

#  b = driver.getelementbyattribute('css selector:.hc_selectbox-tree-div,display:block')
#  css selector:.hc_selectbox-tree-div,style:[\s\S]*display: block;
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
    '''k:鍒楀悕  v:鍒楀�� 
    '''
    i=1
    j=1
    elements=None
    elements=driver.getelementbyattribute('css selector:.hc-datagrid-header>table>tbody>tr>td',getall = True)
    while i<=len(elements):
        tt=driver.getelementbyattribute('css selector:.hc-datagrid-header>table>tbody>tr>td:nth-child('+str(i)+')>div',getall=True)
        xt=tt[0].gettext()   # 閼挎粌宕�
        if xt==k:
            break
        i=i+1
    
    element1s=driver.getelementbyattribute('css selector:.hc-datagrid-body>table>tbody>tr',getall=True)
    while j<=len(element1s):    
        ts=driver.getelementbyattribute('css selector:.hc-datagrid-body>table>tbody>tr:nth-child('+str(j)+')>td:nth-child('+str(i)+')',getall = True)
        xs=ts[0].gettext()   # 閼挎粌宕�
        
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
  
if __name__ == '__main__':
    global driver
    driver=ClassSelenium.ClassSelenium("http://192.168.70.237:8080/am/login.htm,chrome")
    driver.getelementbyattribute("id:vc_op_code").sendkeys('8888')
    driver.getelementbyattribute('id:vc_op_password').sendkeys("123456")   #��
    driver.getelementbyattribute('id:login').Click()
    driver.getelementbyattribute('link text:系统管理').Click()#菜单
    driver.getelementbyattribute('link text:系统配置管理').Click()#菜单
    driver.getelementbyattribute('link text:系统开关配置').Click()#菜单
    #閼惧嘲褰囬悽銊﹀煕鐞涖劌宕�
    global operatable
#     operatable=driver.getelementbyattribute('tag name:table,id:data_table_dataTable')
    #閼惧嘲褰囬悽銊﹀煕閸旂喕鍏橀懣婊冨礋
    global buttonmenu
    # buttonmenu=driver.getelementbyattribute("xpath:.//*[@id='wrap_dataTable']/div[1]")
    # #閼惧嘲褰囩悰銊ュ礋婢讹拷
    # tableheader = driver.getelementbyattribute("id:head_dataTable")
    # tableheadername =  getheaderlist(tableheader)
    # print(tableheadername)
    # ab = driver.getelementbyattribute(r"xpath:.//*[@id='head_dataTable']/tbody/tr/td[12]/div").gettext()
    # print(ab)
    # #閼惧嘲褰囩悰銊ュ礋娴ｏ拷
    # tablebody = driver.getelementbyattribute("id:data_table_dataTable")
    attrlist=['tag name','partial link text','link text','class name','id','name','css selector','xpath']
    attrdes=':[^,]*','css selector:.hc-datagrid-header>#head_dataTable>tbody>tr>td:nth-child(15)>div'
    #浠庡睘鎬у瓧绗︿覆涓壘鍑轰富灞炴�э紝浼樺厛鎵惧嚭tag name
#     for attrstr in attrlist:
#         if re.search(attrstr+':[^,]*',attrdes):
#             primary=re.search(attrstr+':[^,]*', attrdes).group()
#             assist=attrdes.replace(primary,'').strip(',')
#             #assist=re.sub(primary+':[^,]*', '', attrdes).strip(',')
#             break   
#     primaryindex=primary.index(":")
#     driver.getelementbyattribute('css selector:.hc-datagrid-header>#head_dataTable>tbody>tr>td:nth-child(15)>div').gettabletext()
    a,b = getheaderlist()
    print(a,b)
    pass