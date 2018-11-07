import unittest
from SecondWeekTest import test1
from registerCase import register
'''
使用继承unittest的方式进行测试套件的开发
'''

class all_case(unittest.TestCase):
    # case_dir = r"F:\PythonTest\register.py"
    def setUp(self,nickname,email,password):
        self.register = register.test_admin_register(nickname,email,password)
    # 名字要规范，一般变量使用下划线xxx_xxx
    test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_case,pattern='test*.py',top_level_dir=None)
    for test_suit in discover:
        for test_case in test_suit:
            test_case.addTest(test_case)
            print(test_case)
if __name__ == "__main__":
    #返回实例
    runner = unittest.TextTestRunner()
    #run所有用例
    runner.run(all_case())