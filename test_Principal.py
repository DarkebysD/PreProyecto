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

# validar titulo de la pagina
def test_validar_titulo(driver):
    titulo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert titulo.text == "Swag Labs", "El título es el esperado"

# validar que el menú de navegación esté presente
def test_validar_menu(driver):
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menú de navegación está presente"

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






