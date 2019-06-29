class BaseView(object):
    def __init__(self,driver):
        self.driver=driver
    def find_elements(self,*loc):
        return self.find_element(*loc)
    def find_element(self,*loc):
        return self.find_element(*loc)
    def get_window_size(self):
        return self.driver.get_window_size()
    def swipe(self,start_x,start_y,end_x,end_y,duration):
        return self.driver.swipe(start_x,start_y,end_x,end_y,duration)
    def sendKeyEvent(self,*keycode):
        return self.driver.sendKeyEvent(*keycode);