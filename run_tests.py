import unittest
from HTMLTestRunner import HTMLTestRunner


test_dir = "./test_case"
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test_data_center.py')
if __name__ == '__main__':
    fp = open('./test_report/result.html', 'wb')
    # runner = unittest.TextTestRunner(verbosity=2)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告")
    runner.run(suits)
    fp.close()
