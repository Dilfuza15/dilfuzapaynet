from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.phone_number = (By.NAME, "phone")
        self.btn_submit = (By.CSS_SELECTOR, "button[type='submit']")
        self.password = (By.NAME, "password")
        self.dropdown = (By.CLASS_NAME, "drop-down-component")
        self.btn_finish = (By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(2) > div.drop-down-component__content > div.sessions__item-content > button")


    def enter_phone_number(self, phone_number):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((self.phone_number))).send_keys(phone_number)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((self.password))).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.btn_submit)
        ).click()

    def find_dropdown(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((self.dropdown))
        ).click()

    def click_btn_finish(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((self.btn_finish))
        ).click()