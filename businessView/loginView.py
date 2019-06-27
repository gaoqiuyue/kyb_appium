#coding=utf-8
import logging
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.common_func import Common
from common.desired_caps import appium_desired


class LoginView(Common):
    username_type=(By.ID,"com.tal.kaoyan:id/login_email_edittext")
    password_type=(By.ID,"com.tal.kaoyan:id/login_password_edittext")
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')
    myBtn=(By.ID,"com.tal.kaoyan:id/mainactivity_button_mysefl")
    userinfo=(By.ID,"com.tal.kaoyan:id/activity_usercenter_username")
    # 退出操作相关元素
    settingBtn = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButtonWraper')
    logoutBtn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    # 个人中心下线警告提醒确定按钮
    commitBtn = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()
        logging.info("======login========")
        logging.info("input username%s"%username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info("input password%s" % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info("click loginBtn")
        self.driver.find_element(*self.loginBtn).click()
        logging.info("========login finished=========")
    def check_account_alert(self):
        ##检测是否有用户下线提示
        logging.info('====check_account_alert======')
        try:
            WebDriverWait(driver, 10).until(lambda x: x.find_element(*self.commitBtn))
        except TimeoutException:
            pass
        except NoSuchElementException:
            pass
        else:
            driver.find_element(*self.commitBtn).click()
        # try:
        #     element = self.driver.find_element(*self.commitBtn)
        # except NoSuchElementException:
        #     pass
        # else:
        #     logging.info('click commitBtn')
        #     element.click()
    def check_loginStatus(self):
        logging.info('==========check_loginStatus===========')
        self.check_market_ad()
        #time.sleep(30)
        self.check_account_alert()
        #登录成功后，点击我的，查看用户名
        try:
            self.driver.find_element(*self.myBtn).click()
            self.driver.find_element(*self.userinfo)
        except NoSuchElementException:
            logging.info("login failed")
            self.getScreenShot("login Fail")
            return False
        else:
            logging.info("login success")
            l.logout_action()
            return True
    def logout_action(self):
        self.driver.find_element(*self.settingBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()



if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action("susugao","gao123456")
    l.check_loginStatus()
