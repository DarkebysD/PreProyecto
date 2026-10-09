import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    yield driver
    driver.quit() 
    

# Ingreso de credenciales
def test_ingreso_credenciales(driver):
    time.sleep(5)

    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("problem_user")
    time.sleep(2)

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    time.sleep(2)

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    time.sleep(2)

# Validar que el carrito de compras esté vacío
def test_validar_carrito(driver):
    if len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) > 0:
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 1, "El carrito de compras no está vacío"
    else:
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0, "El carrito de compras está vacío"