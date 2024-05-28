from selenium.webdriver.common.by import By

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu_option_xpath = (By.XPATH, '//a[@href="/web/index.php/pim/viewPimModule"]')
        self.delete_option_xpath = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[9]/div/div[9]/div/button[1]/i')
        self.delete_button_xpath = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')

    def navigate_to_pim(self):
        try:
            self.driver.find_element(*self.pim_menu_option_xpath).click()
        except Exception as e:
            print(f"Error navigating to PIM: {e}")

    def click_delete_option(self):
        try:
            self.driver.find_element(*self.delete_option_xpath).click()
        except Exception as e:
            print(f"Error clicking delete option: {e}")

    def confirm_delete(self):
        try:
            self.driver.find_element(*self.delete_button_xpath).click()
        except Exception as e:
            print(f"Error confirming delete: {e}")
