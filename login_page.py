from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.NAME, 'username')
        self.password_locator = (By.NAME, 'password')
        self.submit_button_locator = (By.XPATH, '//button[@type="submit"]')
    
    def enter_username(self, username):
        try:
            self.driver.find_element(*self.username_locator).send_keys(username)
        except Exception as e:
            print(f"Error entering username: {e}")
    
    def enter_password(self, password):
        try:
            self.driver.find_element(*self.password_locator).send_keys(password)
        except Exception as e:
            print(f"Error entering password: {e}")

    def click_login(self):
        try:
            self.driver.find_element(*self.submit_button_locator).click()
        except Exception as e:
            print(f"Error clicking login button: {e}")
