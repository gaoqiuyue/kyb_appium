#coding=utf-8
import csv
import os
import time


import logging

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from baseView.baseView import BaseView
from common.desired_caps import appium_desired


class Common(BaseView):
    #取消和跳过引导按钮
    cancelBtn=(By.ID,"android:id/button2")
    skipBtn = (By.ID,"com.tal.kaoyan:id/tv_skip")
    #登录后浮窗广告取消按钮
    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/task_no_task')
    def check_cancelBtn(self):
        logging.info("=========check_cancelBtn=======")
        try:
            cancelBtn=self.driver.find_element(*self.cancelBtn)
        except Exception:
            logging.info("no cancelBtn")
        else:
            logging.info("click cancelBtn")
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info("=========check_skipBtn=======")
        try:
            skipBtn=self.driver.find_element(*self.skipBtn)
        except Exception:
            logging.info("no skipBtn")
        else:
            logging.info("click cancelBtn")
            skipBtn.click()

    def get_screenSize(self):
        x=self.get_window_size()['width']
        y=self.get_window_size()['height']
        return (x,y)
    def swipeLeft(self):
        logging.info("swipeLeft")
        x,y=self.get_screenSize()

        print(x,y)
        x1=int(x*0.9)
        x2=int(x*0.2)
        y1=int(y*0.5)
        self.swipe(x1,y1,x2,y1,1000)
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now
    def getScreenShot(self,module):
        time=self.getTime()
        image_path=os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png'%(module,time)
        print(image_path)
        logging.info("get screenshot")
        self.driver.get_screenshot_as_file(image_path)

    def check_market_ad(self):
        '''检测登录或者注册之后的界面浮窗广告'''
        logging.info('=======check_market_ad=============')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()
    def get_csv_data(self,csv_file,line):
        #获取指定行数据
        with open(csv_file,'r',encoding='utf-8-sig')as fp:
            reader=csv.reader(fp)
            for index,row in(enumerate(reader,1)):
                if index==line:
                    return row

    # csv_file = '../data/account.csv'
    # data = get_csv_data(csv_file, 3)
    # print(data)


if __name__ == '__main__':
    driver=appium_desired()
    comm=Common(driver)
    # comm.check_cancelBtn()
    # comm.swipeLeft()
    # comm.getScreenShot("startapp")
    #comm.check_skipBtn()
