from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "(//button[normalize-space()='Login'])[1]"
    el_dropdown_CLASSNAME = "oxd-userdropdown"
    link_logout_LINKTEXT = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_dropdown(self):
        self.driver.find_element(By.CLASS_NAME, self.el_dropdown_CLASSNAME).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_LINKTEXT).click()
