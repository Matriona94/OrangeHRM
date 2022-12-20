from page_objects.login_page import LoginPage
import pytest


class Test001Login:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "OrangeHRM":
            assert True
        else:
            assert False

    def test_login_test(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.lp.click_dropdown()
        self.lp.click_logout()

