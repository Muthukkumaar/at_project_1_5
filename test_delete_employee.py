import pytest
from utils.driver import get_driver
from pages.login_page import LoginPage
from pages.pim_page import PimPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_delete_employee(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    login_page = LoginPage(driver)
    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    login_page.click_login()

    pim_page = PimPage(driver)
    pim_page.navigate_to_pim()
    pim_page.click_delete_option()
    pim_page.confirm_delete()