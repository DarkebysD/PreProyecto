import pytest
from test_credenciales import driver, test_ingreso_credenciales
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="module")

 # validar que el menú de navegación esté presente
def test_validar_menu(driver):
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menú de navegación está presente"