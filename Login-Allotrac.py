import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://dummy.allotrac.com/login")
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()
    assert "dashboard" in driver.current_url

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("wronguser")
    login_page.enter_password("wrongpassword")
    login_page.click_login()
    assert "Invalid credentials" in driver.page_source
