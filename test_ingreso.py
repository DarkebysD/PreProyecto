import pytest
from test_credenciales import driver, test_ingreso_credenciales
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="module")
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