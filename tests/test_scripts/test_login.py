import time
import pytest
import time
import random
from selenium import webdriver

from page_objects.login_page import LoginPage

from utilities.read_properties import ReadLoginConfig

from utilities.custom_logger import LogGen


class TestLogin:
    login_config = ReadLoginConfig()
    base_url = login_config.get_login_info('base_url')
    logger = LogGen.loggen()

    username_text = login_config.get_login_info('username_text')
    password_text = login_config.get_login_info('password_text')

    @pytest.fixture(autouse=False)
    def setup_test_script(self):
        yield
        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_page_visibility_bad(self, setup):
        self.logger.info("test_login_page_visibility_bad *** START")
        self.driver = setup
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        time.sleep(1)
        self.lp.logo_top_visibility_bad()
        self.logger.info("test_login_page_visibility_bad *** END")

    @pytest.mark.regression
    def test_login_page(self, setup):
        self.logger.info("test_login_page *** START")
        self.driver = setup
        self.driver.get(self.base_url)

        self.lp = LoginPage(self.driver)
        self.lp.check_url()
        self.lp.login_page_visibility()

        self.lp.click_login_button()
        self.lp.message_invalid_required_username()
        self.lp.message_invalid_required_password()

        self.lp.input_random_username()
        self.lp.input_random_password()
        self.lp.click_login_button()
        self.lp.message_invalid_credentials()

        self.lp.input_paragraph_username()
        self.lp.input_paragraph_password()
        self.lp.click_login_button()

        # self.lp.input_username(self.username_text)
        # self.lp.input_password(self.password_text)
        # self.lp.click_login_button()


