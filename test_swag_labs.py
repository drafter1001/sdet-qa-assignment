
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSwagLabs:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(self.driver, 5)
        yield
        self.driver.quit()

    def test_valid_user_login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        page_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title"))).text
        assert page_title == "Products"

    def test_locked_out_user_error(self):
        self.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        error_msg = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        assert "Epic sadface" in error_msg.text
