from selenium.webdriver.common.by import By


class BaseView(object):
    black_list=[(By.ID,"android:id/button2"),
    (By.ID,"com.tal.kaoyan:id/tv_skip")]
    def __init__(self,driver):
        self.driver=driver
    def find_elements(self,*loc):
        return self.find_element(*loc)

    def find_element_exception(self, locator):
        #查找元素，如果出现弹窗等异常流程，跳入异常处理流程
        print(locator)
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            # self.find_element(locator)
            return self.driver.find_element(*locator)
    def find_element(self,*loc):
        return self.find_element(*loc)
    def get_window_size(self):
        return self.driver.get_window_size()
    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.driver.swipe(start_x,start_y,end_x,end_y,duration)

    def handle_exception(self):
        #从黑名单中读取元素定位，如跳过的按钮，或者取消升级的按钮
        print(":exception")
        self.driver.implicitly_wait(0)
        for locator in self._black_list:
            print(locator)
            elements = self.driver.find_elements(*locator)

            if len(elements) >= 1:
                # todo: 不是所有的弹框处理都是要点击弹框，可根据业务需要自行封装
                elements[0].click()
            else:
                print("%s not found" % str(locator))

            # todo: 私用page source会更快的定位

            # page_source=self.driver.page_source
            # if "image_cancel" in page_source:
            #     self.driver.find_element(*locator).click()
            # elif "tips" in page_source:
            #     pass