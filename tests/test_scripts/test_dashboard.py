from page_objects.login_page import LoginPage
import pytest
from page_objects.dashboard_main_menu import DashboardMainMenu
from utilities.read_properties import ReadLoginConfig


class Test002Dashboard:
    baseURL = ReadLoginConfig.get_base_url()
    username = ReadLoginConfig.get_username()
    password = ReadLoginConfig.get_password()

    def test_dashboard_test(self, setup):
        self.driver = setup
        self.dm = DashboardMainMenu(self.driver)
        self.dm.click_admin()
        self.dm.click_pim()
        self.dm.click_leave()
        self.dm.click_time()
        self.dm.click_recruitment()
        self.dm.click_my_info()
        self.dm.click_performance()
        self.dm.click_dashboard()
        self.dm.click_directory()
        self.dm.click_maintenance()
        self.dm.click_buzz()

