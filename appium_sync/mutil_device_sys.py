#coding=utf-8
from time import ctime
import yaml
from appium import webdriver
import  logging
import logging.config
import os
import multiprocessing
CON_LOG="../config/log.conf"
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
devices_list = ['127.0.0.1:62001', '127.0.0.1:21503']
def appium_desired(udid,port):
    with open("../config/kyb_caps.yaml",'r',encoding='utf-8')as fp:
        data=yaml.load(fp)
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid'] = udid
    #os.path.dirname(__file__)---获得当前文件的父目录
    base_dir=os.path.dirname(os.path.dirname(__file__))
    app_path=os.path.join(base_dir,'app',data['appname'])
    desired_caps['app']=app_path
    desired_caps['noReset']=data['noReset']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['automationName'] = data['automationName']
    print('appium port: %s start run %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver
desired_process=[]
for i in range(len(devices_list)):
    port=4723+i*2
    desired=multiprocessing.Process(target=appium_desired,args=(devices_list[i],port))
    desired_process.append(desired)

if __name__ == '__main__':
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()