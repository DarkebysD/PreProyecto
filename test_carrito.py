import pytest
from test_credenciales import driver, test_ingreso_credenciales
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="module")

# Validar que el carrito de compras esté vacío
def test_validar_carrito(driver):
    if len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) > 0:
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 1, "El carrito de compras no está vacío"
    else:
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0, "El carrito de compras está vacío"

# Agregar un producto al carrito
def test_agregar_producto_al_carrito(driver):
    agregar_al_carrito_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    agregar_al_carrito_button.click()
    time.sleep(2)

# Validar que el carrito de compras tenga un producto
def test_validar_carrito_con_producto(driver):   
    if len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) > 0:
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 1, "El carrito de compras no está vacío"
    else:
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0, "Error: El carrito de compras está vacío después de agregar un producto"