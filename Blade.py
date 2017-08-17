#coding=utf-8

import json,sys,configparser
from Lib.Common import rootpath
import time

def readConfigFile(section,option):
    """
    sections:配置文件中[]中的值
    options:每组中的键
    """
    config = configparser.ConfigParser()
    config.readfp(open(rootpath+'\Blade.ini'))
    try:
        value=config.get(section,option)
    except configparser.NoSectionError:
        value=None
    return value
    
def writeConfigFile(section,option,value):
    config = configparser.ConfigParser()
    config.readfp(open(rootpath+'\Blade.ini'))
    config.set(section,option,value)
    config.write(open(rootpath+'\Blade.ini', "w"))

if __name__ == '__main__': 
    while True:
        try:
            JavaRunFlag=readConfigFile('Selenium','JavaRunFlag')
            if JavaRunFlag.upper()=='EXIT':
                break
            elif JavaRunFlag.upper()=='STOP':
                time.sleep(1)
            elif JavaRunFlag.upper()=='START':
                InputData={}
                UIExcept={}
                FunName=readConfigFile('Selenium','JavaRunMethodName')
                InputDatastr=readConfigFile('Selenium','InputData')
                LibName=readConfigFile('Selenium','JavaRunClassName')
                UIExceptstr=readConfigFile('Selenium','UIExcept')
                #数据处理
                FunName=FunName.strip('.')
                LibName=LibName.strip('.')
                UIExceptList=UIExceptstr.split(";")
                for each in UIExceptList:
                    eachlist=each.split('=',1)
                    UIExcept[eachlist[0]]=eachlist[1]
                InputDataList=InputDatastr.split("|")
                for each in InputDataList:
                    eachlist=each.split('=',1)
                    InputData[eachlist[0]]=eachlist[1]
                exec('import '+LibName)
                
                exec(LibName+'.InputData=InputData')
                exec(LibName+'.UIExcept=UIExcept')
                result,message=eval(LibName+'.'+FunName+'()')
                print(result,message)
                writeConfigFile('Selenium','JavaRunFlag','Stop')
                writeConfigFile('Selenium','JavaReturnFlag',result)
                writeConfigFile('Selenium','JavaReturnValue',message)
        except Exception as e:
            writeConfigFile('Selenium','JavaRunFlag','Stop')
            writeConfigFile('Selenium','JavaReturnFlag','Fail')
            writeConfigFile('Selenium','JavaReturnValue',str(e))
        
        
        
        
        
        
        
        