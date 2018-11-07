from registerCase.register import register
from webDriver import driver
class test1():

    def test1(self):
        url = "https://rd.bosma.cn/uc/#/welcome"
        url = driver.get(url)#知道了吧
        user_file = open('registerUser.txt','r')
        line = user_file.readline()
        nickname = line.split(',')[0]
        email = line.split(',')[1]
        password = line.split(',')[2]
        print(email)
        print(password)
        #LoginTest().admin_login(email,password)
        register().test_admin_register(nickname,email,password)
# if __name__ == '__main__':
#     test = test1()
#     test.test1()


