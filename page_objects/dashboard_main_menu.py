from selenium.webdriver.common.by import By
from selenium import webdriver


class DashboardMainMenu:
    main_menu_admin_xpath = "//a[@class='oxd-main-menu-item active']//span[1]"
    main_menu_PIM_xpath = "//span[normalize-space()='PIM']"
    main_menu_leave_xpath = "//span[normalize-space()='Leave']"
    main_menu_time_xpath = "//span[normalize-space()='Time']"
    main_menu_recruitment_xpath = "//span[normalize-space()='Recruitment']"
    main_menu_my_info_xpath = "//span[normalize-space()='My Info']"
    main_menu_performance_xpath = " //span[normalize-space()='Performance']"
    main_menu_dashboard_xpath = "//span[normalize-space()='Dashboard']"
    main_menu_directory_xpath = "//span[normalize-space()='Directory']"
    main_menu_maintenance_xpath = "//span[normalize-space()='Maintenance']"
    main_menu_buzz_xpath = " //span[normalize-space()='Buzz']"

    def __init__(self, driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.XPATH, self.main_menu_admin_xpath).click()

    def click_pim(self):
        self.driver.find_element(By.XPATH, self.main_menu_PIM_xpath).click()

    def click_leave(self):
        self.driver.find_element(By.XPATH, self.main_menu_leave_xpath).click()

    def click_time(self):
        self.driver.find_element(By.XPATH, self.main_menu_time_xpath).click()

    def click_recruitment(self):
        self.driver.find_element(By.XPATH, self.main_menu_recruitment_xpath).click()

    def click_my_info(self):
        self.driver.find_element(By.XPATH, self.main_menu_my_info_xpath).click()

    def click_performance(self):
        self.driver.find_element(By.XPATH, self.main_menu_performance_xpath).click()

    def click_dashboard(self):
        self.driver.find_element(By.XPATH, self.main_menu_dashboard_xpath).click()

    def click_directory(self):
        self.driver.find_element(By.XPATH, self.main_menu_directory_xpath).click()

    def click_maintenance(self):
        self.driver.find_element(By.XPATH, self.main_menu_maintenance_xpath).click()

    def click_buzz(self):
        self.driver.find_element(By.XPATH, self.main_menu_buzz_xpath).click()
