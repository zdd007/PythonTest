import unittest
from registerCase.Register import register

def run():
    case_dir = r"F:\PythonTest\registerCase\Register.py"
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='*.py', top_level_dir=None)
    for test_case in discover:
            suite.addTest(register.register('test_admin_register'))

# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
