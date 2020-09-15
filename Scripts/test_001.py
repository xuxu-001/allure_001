import allure
from selenium import webdriver


class Test(object):

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')

    @allure.step('第二步')
    def abc(self):
        print('我和你')

    @allure.step('第一步')
    def test_001(self):
        self.abc()
        # 添加截图
        allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        print('\n ---test_001')
