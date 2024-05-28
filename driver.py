from selenium import webdriver

def get_driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    return driver
