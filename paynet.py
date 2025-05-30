from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Тест 1 — Проверка заголовка
def test_title_contains_paynet():
    driver = webdriver.Chrome()
    driver.get("https://www.paynet.uz/")
    WebDriverWait(driver, 10).until(EC.title_contains("Paynet"))
    assert "Paynet" in driver.title
    driver.quit()

# Тест 2 — Проверка логотипа (по классу nav-logo)
def test_logo_is_visible():
    driver = webdriver.Chrome()
    driver.get("https://www.paynet.uz/")
    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "nav-logo"))
    )
    assert logo.is_displayed()
    driver.quit()

# Тест 3 — Переключение языка (проверим изменение URL на /uz)

def test_language_switch_to_uz():
    driver = webdriver.Chrome()
    driver.get("https://www.paynet.uz/")

    wait = WebDriverWait(driver, 20)

    # Шаг 1: Клик по кнопке раскрытия меню языков
    lang_dropdown = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "w-dropdown-toggle"))
    )
    lang_dropdown.click()

# Тест 4 — Переключение языка (проверим изменение URL на /ru)
def test_language_switch_to_ru():
    driver = webdriver.Chrome()
    driver.get("https://wwww.paynet.uz/")

    wait = WebDriverWait(driver, 20)

    # Шаг 1: Клик по кнопке расрытия меню языков
    Lang_dropdown = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "w-dropdown-toggle"))
    )
    lang_dropdown.click()
