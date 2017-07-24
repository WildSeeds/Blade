# coding=utf-8
'''
Created on 2015年6月10号

@author: Administrator
'''
import sys
import os

# import configparser
#rootpath = sys.path[0]
if getattr(sys, 'frozen', False):
    rootpath = os.path.dirname(sys.executable)
elif __file__:
    rootpath = os.path.dirname(__file__)
    print(rootpath)
    rootpath=os.path.dirname(rootpath)
    print(rootpath)
flag=os.sep
# 将当前路径加入搜索路径
testplanfolder=rootpath + flag+'TestPlan'+ flag
testplanfilepath =testplanfolder+'TestConfig.xlsx'
configfolder=rootpath + flag+r'Config'+ flag
configfilepath = configfolder+'Config.xlsx'
resultfilepath = rootpath + flag+'Result'+ flag
testcasefilepath = rootpath + flag+'TestCase'+ flag
logfilepath = resultfilepath+'TestResult.xlsx'
toolfolderpath = rootpath + flag+'Tool'+ flag
screenshotpath = rootpath + flag+'Screenshot'+ flag
logpath = rootpath + flag+'log'+ flag
screenpath = rootpath + flag+'Screenshot'+ flag+'screen'+ flag
differpath = rootpath + flag+'Screenshot'+ flag+'differ'+ flag
testdatapath = rootpath + flag + 'TestData' + flag
case_data_folder_path = testdatapath +'CaseData' + flag
# 执行结果
ACTIONFAIL = 'FAIL'
ACTIONPASS = 'PASS'
ACTIONERROR='ERROR'
REVARSTR=r'[lgLG][Vv]_[0-9a-zA-Z_]+'
REVARATTACHSTR=r'(?:\$[0-9a-zA-Z,_$\.\-\:\s\\\u4e00-\u9fa5]+)*'
REVARATTACHSTR_GROUP=r'(?:\$([0-9a-zA-Z,_$\.\-\s\:\\\u4e00-\u9fa5]+))*'
CASEDATASTR='(?:[a-zA-Z0-9_\u4e00-\u9fa5]+\.){0,1}'
CASEDATASTR_GROUP='(?:([a-zA-Z0-9_\u4e00-\u9fa5]+)\.){0,1}'
TIMEOUT = 20