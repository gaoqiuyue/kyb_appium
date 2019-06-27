import random
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.common_func import Common
from common.desired_caps import logging, appium_desired


class RegisterView(Common):
    #登录页面注册元素
    register_text=(By.ID,"com.tal.kaoyan:id/login_register_text")
    #头像设置相关
    userheader=(By.ID,"com.tal.kaoyan:id/activity_register_userheader")
    imageView=(By.ID,"com.tal.kaoyan:id/item_image")
    saveBtn=(By.ID,"com.tal.kaoyan:id/save")
    #注册页面元素
    username = (By.ID,"com.tal.kaoyan:id/activity_register_username_edittext")
    password=(By.ID,"com.tal.kaoyan:id/activity_register_password_edittext")
    email=(By.ID,"com.tal.kaoyan:id/activity_register_email_edittext")
    registerBtn=(By.ID,"com.tal.kaoyan:id/activity_register_register_btn")
    ##完善列表页面信息
    school_name=(By.ID,"com.tal.kaoyan:id/perfectinfomation_edit_school_name")
    major=(By.ID, "com.tal.kaoyan:id/activity_perfectinfomation_major")
    goBtn=(By.ID,"com.tal.kaoyan:id/activity_perfectinfomation_goBtn")
    #院校列表
    city=(By.ID,"com.tal.kaoyan:id/more_forum_title")
    school = (By.ID, "com.tal.kaoyan:id/university_search_item_name")
    #专业列表
    major_subject_title = (By.ID, "com.tal.kaoyan:id/major_subject_title")
    major_group_title = (By.ID, "com.tal.kaoyan:id/major_group_title")
    major_search_item_name = (By.ID, "com.tal.kaoyan:id/major_search_item_name")
    #个人中心
    myBtn = (By.ID, "com.tal.kaoyan:id/mainactivity_button_mysefl")
    userinfo = (By.ID, "com.tal.kaoyan:id/activity_usercenter_username")
    def register_action(self,username,password,email):
        self.check_cancelBtn()
        self.check_skipBtn()
        logging.info("点击注册按钮")
        self.driver.find_element(*self.register_text).click()

        ###填写注册信息
        logging.info("register_usename is %s"%username)
        self.driver.find_element(*self.username).send_keys(username)
        time.sleep(2)
        logging.info("register_password is %s" % password)
        self.driver.find_element(*self.password).send_keys(password)
        time.sleep(2)
        logging.info("register_email is %s" % email)
        self.driver.find_element(*self.email).send_keys(email)
        time.sleep(2)
        # ##选择头像
        # logging.info('set userheader')
        # self.driver.find_element(*self.userheader).click()
        # logging.info("=======loading images==========")
        # # time.sleep(30)
        # self.driver.find_elements(*self.imageView)[1].click()
        # self.driver.find_element(*self.saveBtn).click()
        logging.info('点击注册按钮')
        self.driver.find_element(*self.registerBtn).click()
        #time.sleep(3)
        ##判断是否进入到完善信息界面--注册太频繁会被限制无法进入该界面
        try:
            self.driver.find_element(*self.school_name)
        except  NoSuchElementException:
            logging.info("register failed")
            self.getScreenShot("register failed")
            return False
        else:
            self.add_register_info()
            # 注册结果判断
            if self.check_registerStatus():
                return True
            else:
                return False
    def add_register_info(self):
        logging.info("=======choose schoolname======")
        self.driver.find_element(*self.school_name).click()
        self.driver.find_elements(*self.city)[1].click()
        self.driver.find_elements(*self.school)[1].click()
        logging.info("=======choose major======")
        self.driver.find_element(*self.major).click()
        self.driver.find_elements(*self.major_subject_title)[1].click()
        self.driver.find_elements(*self.major_group_title)[1].click()
        self.driver.find_elements(*self.major_search_item_name)[1].click()
        logging.info("=======click gobtn======")
        self.driver.find_element(*self.goBtn).click()
    def check_registerStatus(self):
        self.check_market_ad()
        logging.info('==========check_registerStatus===========')
        try:
            self.driver.find_element(*self.myBtn).click()
            self.driver.find_element(*self.userinfo)
        except NoSuchElementException:
            logging.info("register failed")
            self.getScreenShot("register Fail")
            return False
        else:
            logging.info("register success")
            self.getScreenShot("register success")
            return True
if __name__ == '__main__':
    driver=appium_desired()
    register=RegisterView(driver)
    username = str('qyy2018' + str(random.randint(1000, 9000)))
    password = str('qiuyue' + str(random.randint(1000, 9000)))
    email = str('31623' + str(random.randint(1000, 9000)) + '@qq.com')
    register.register_action(username,password,email)
    #register.register_action("sususu123","gao123456","315442611@qq.com")