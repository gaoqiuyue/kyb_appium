from appium import webdriver


class TestWeb:

    def setup(self):
        caps={}
        caps["browserName"]="Chrome"
        caps["deviceName"]="127.0.0.1:21503"
        caps["platformName"]="android"
        caps["chromedriverExecutable"]=r"D:\Program\driver\39\chromedriver.exe"
        caps["showChromedriverLog"] = True
        # caps["noReset"]=True


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_testerhome_search(self):
        self.driver.get("https://www.baidu.com")
        #self.driver.switch_to.context("NATIVE_APP")
        #self.driver.find_element_by_id("com.android.chrome:id/button_secondary").click()
        #self.driver.switch_to.context(self.driver.contexts[1])
        #print(self.driver.current_context)
        #print(self.driver.page_source)
        # self.driver.find_element_by_link_text("Sign In").click()

        self.driver.find_element_by_css_selector("#mobile-search-form > input").send_keys("hogwarts")