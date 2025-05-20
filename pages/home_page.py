from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile = (By.CSS_SELECTOR, "#app > div > div.header > div > div.header__avatar")


    def click_profile(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.profile)
        ).click()
