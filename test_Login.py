from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def test_login():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

# Ingreso de credenciales
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

    if wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))):
        print("Ingreso exitoso")
    else:
        print("Ingreso fallido")
    
#validar Url de la pagina
    
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "La URL es la esperada"

# validar titulo de la pagina

    titulo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert titulo.text == "Swag Labs", "El título es el esperado"

# validar que el menú de navegación esté presente
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed(), "El menú de navegación está presente"

# Validar que el carrito de compras esté vacío
    if len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) > 0:
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 1, "El carrito de compras no está vacío"
    else:
        assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0, "El carrito de compras está vacío"

# validar filtros de productos

    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed(), "El filtro de productos está presente"

# validar productos

    Producto1 = driver.find_element(By.ID, "item_4_title_link")
    assert Producto1.text == "Sauce Labs Backpack", "El producto es el esperado"

    Producto2 = driver.find_element(By.ID, "item_2_title_link")
    assert Producto2.text == "Sauce Labs Onesie", "El producto es el esperado"

    try:
      ProductoError = driver.find_element(By.ID, "item_9_title_link")
      assert ProductoError.text == "Producto no existente"  
    except NoSuchElementException: 
      print("El producto no existe")
    

    driver.quit()






