import pytest
from test_credenciales import driver, test_ingreso_credenciales
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="module")

# validar titulo de la pagina
def test_validar_titulo(driver):
    wait = WebDriverWait(driver, 10)
    titulo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert titulo.text == "Swag Labs", "El título es el esperado"