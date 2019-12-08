import csv
from time import sleep

import pytest
from businessView.loginView import LoginView
from common.desired_caps import logging, appium_desired
from common.myunit import StartEnd
class LoginTest():
    def setUp(self):
        logging.info('======setUp=========')
        self.driver=appium_desired()


    def tearDown(self):
        logging.info('======tearDown=====')
        sleep(5)
        self.driver.close_app()
    def read_csv(path):
        test_data = []

        with open(path) as f:
            csv_data=csv.reader(f)
            for row in csv_data:  # 将csv 文件中的数据保存到birth_data中
                test_data.append(row)
        return test_data

    csv_path = "../data/kybaccount.csv"
    csv_data=read_csv(path=csv_path)
    @pytest.mark.parametrize("username,password",csv_data)
    def test_login(self,username,password):
        l = LoginView(self.driver)
        l.login_action(username=username,password=password)
        self.assertTrue(l.check_loginStatus())
    @pytest.mark.parametrize("username,password",[
        ("susu","gao123"),
        ("yiner","test12345")
    ])
    def test_login_test1(self):
        l=LoginView(self.driver)
        data=l.get_csv_data(self.csv_file,1)
        l.login_action(data[0],data[1])
        self.assertTrue(l.check_loginStatus())

    def test_login_test2(self):
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

    def test_login_test3(self):
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_loginStatus())

# if __name__ == '__main__':
#     unittest.main()
