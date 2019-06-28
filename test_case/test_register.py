import random
import unittest

from businessView.registerView import RegisterView
from common.desired_caps import logging
from common.myunit import StartEnd


class Register_test(StartEnd):
    def test_user_register(self):
        logging.info("=========test_user_register===========")
        r=RegisterView(self.driver)
        username="susg"+"YE"+str(random.randint(1000,9999))
        password = "susg" + "YE" + str(random.randint(1000, 9999))
        email = "susg" + "YE" + str(random.randint(1000, 9999))+"@163.com"
        r.register_action(username,password,email)

        self.assertTrue(r.register_action(username,password,email))
if __name__ == '__main__':
    unittest.main()