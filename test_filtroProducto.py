import pytest
from test_credenciales import driver, test_ingreso_credenciales
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="module")
# validar filtros de productos
def test_validar_filtros(driver):
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "El filtro de productos está presente"

# validar productos
def test_validar_productos(driver):
    Producto1 = driver.find_element(By.ID, "item_4_title_link")
    assert Producto1.text == "Sauce Labs Backpack", "El producto es el esperado"

    Producto2 = driver.find_element(By.ID, "item_2_title_link")
    assert Producto2.text == "Sauce Labs Onesie", "El producto es el esperado"

    try:
      ProductoError = driver.find_element(By.ID, "item_9_title_link")
      assert ProductoError.text == "Producto no existente"  
    except NoSuchElementException: 
      print("El producto no existe")