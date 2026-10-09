import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="module")
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

#Validacion de ingreso exitoso
def test_validacion_ingreso(driver):
    wait = WebDriverWait(driver, 10)
    if wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))):
        print("Ingreso exitoso")
    else:
        print("Ingreso fallido")
    
#validar Url de la pagina
def test_validar_url(driver):    
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "La URL es la esperada"