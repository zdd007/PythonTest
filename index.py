import unittest
import HTMLTestRunner
import os
def run_all_case():
    TestSuite = unittest.TestSuite()
    test_dir = r"F:\PythonTest\testcase"
    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test*.py',
        top_level_dir=None
    )
    # 直接加载discover
    TestSuite.addTests(discover)
    print(TestSuite)
    return TestSuite
if __name__ == '__main__':
    report_path = "F:\\PythonTest\\report\\result.html"
    fp = open(report_path,  "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,
                                           title = u'Bosma自动化测试报告',
                                           description = u'用例执行情况:')
    runner.run(run_all_case())
    fp.close()



