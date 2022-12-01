from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_test():
    driver = webdriver.Chrome()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    title = driver.title
    assert title == "OrangeHRM"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="username")
    text_box.send_keys("Admin")
    text_box = driver.find_element(by=By.NAME, value="password")
    text_box.send_keys("admin123")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    submit_button.click()

    driver.quit()

