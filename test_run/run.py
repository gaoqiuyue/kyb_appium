
import HtmlTestRunner
import logging
import time
import unittest
test_dir="../test_case"
report_dir="../reports"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + ' test_register.html'

with open(report_name, 'wb') as f:
    runner = HtmlTestRunner.HTMLTestRunner(stream=f, report_name="Kyb Test Report", descriptions="kyb Andriod app Test Report")
    logging.info("start run testcase...")
    runner.run(discover)

