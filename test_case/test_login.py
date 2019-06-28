import unittest

from businessView.loginView import LoginView
from common.myunit import StartEnd

class LoginTest(StartEnd):
    print("开始加载csv")
    csv_file="../data/kybaccount.csv"
    print("开始执行用例")
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

if __name__ == '__main__':
    unittest.main()
