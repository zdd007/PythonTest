import unittest
from SecondWeekTest import test1
'''
使用继承unittest的方式进行测试套件的开发
'''

class all_case(unittest.TestCase):
    case_dir = r"F:\PythonTest\register.py"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)
    for test_suit in discover:
        for test_case in test_suit:
            testcase.addTest(test_case)
            print(testcase)
if __name__ == "__main__":
    #返回实例
    runner = unittest.TextTestRunner()
    #run所有用例
    runner.run(all_case())