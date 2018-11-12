import unittest


class run_all_case():
    def run(self):
        TestSuite = unittest.TestSuite()
        # TestSuite.addTest(register.test_admin_register(self))
        test_dir = r"F:\PythonTest\testcase"
        discover = unittest.defaultTestLoader.discover(
            start_dir=test_dir,
            pattern='test*.py',
            top_level_dir=None
        )
        for test_case in discover:
            TestSuite.addTests(test_case)
            print(test_case)
        return TestSuite

if __name__ == '__main__':
    # 这个不是单元测试的runner器，这个但方法return的是一个testsiute,需要加入runner才可以，
    run_all_case = run_all_case()
    # 加上单元测试的runner器
    runner = unittest.TextTestRunner()
    # 将testsiute加入runner中执行
    runner.run(run_all_case.run())
    # run_all_case.run()



