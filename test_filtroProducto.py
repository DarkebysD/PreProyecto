from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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