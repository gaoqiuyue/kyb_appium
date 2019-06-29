import unittest

import time,logging
import sys
from BSTestRunner import BSTestRunner

path=r'C:\Users\Henry\PycharmProjects\kyb_appium'
sys.path.append(path)

test_dir='../test_case'
report_dir='../reports'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

# with open(report_name,'w')as f:
#     #runner=BSTestRunner(stream=f,title='Kyb Test Report',description='kyb Android app test report')
#     runner = BSTestRunner(stream=f)
#     logging.info('start run test case...')
#
#
#     runner.run(discover)
fp = open(report_name, 'wb')
runner = BSTestRunner(
            stream=fp,
            title='My unit test',
            description='This demonstrates the report output by BSTestRunner.'
            )

# Use an external stylesheet.
# See the Template_mixin class for more customizable options
runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
runner.run(discover)
fp.close()