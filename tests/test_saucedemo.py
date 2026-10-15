import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture()

def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    yield driver

    driver.quit()

def login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


#Automatización de login
def test_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url , "ERROR: Login failed, user not redirected to inventory page"

def test_login_invalid_user(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source, "ERROR: Invalid login did not show error message"

def test_login_invalid_password(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    driver.find_element(By.ID, "login-button").click()

    assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source, "ERROR: Invalid login did not show error message"

def test_login_empty_fields(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "login-button").click()

    assert "Epic sadface: Username is required" in driver.page_source, "ERROR: Empty login did not show error message"

# Navegación y verificación del catálogo
def test_catalog_navigation(driver):
    login(driver)
   
    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs"
    assert section_title == "Products"

def test_product_visibility(driver):
    login(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0 , "ERROR: No products found on the inventory page"

def test_product_count(driver):
    login(driver)
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    product_count = len(products)

    assert product_count == 6 , f"ERROR: Expected 6 products but found {product_count}"

def test_interface_elements(driver):
    login(driver)
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    filter_button = driver.find_element(By.CLASS_NAME, "product_sort_container")
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")

    assert menu_button.is_displayed() , "ERROR: Menu button is not visible"
    assert filter_button.is_displayed() , "ERROR: Filter button is not visible"
    assert cart_button.is_displayed() , "ERROR: Cart button is not visible"

# Interacción con productos y carrito de compras
def test_add_to_cart(driver):
    login(driver)

    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]

    add_to_cart_button = first_item.find_element(By.TAG_NAME, "button")
    add_to_cart_button.click()

    updated_button = first_item.find_element(By.TAG_NAME, "button")

    assert updated_button.text == "Remove", \
        "ERROR: Add to cart button did not change to 'Remove' after clicking"

def test_cart_badge(driver):
    login(driver)

    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    first_item.find_element(By.TAG_NAME, "button").click()
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert cart_badge.is_displayed() , "ERROR: Cart badge is not visible after adding product to cart"
    assert cart_badge.text == "1" , f"ERROR: Expected cart badge to show '1' but got '{cart_badge.text}'"

def test_cart_navigation(driver):
    login(driver)

    first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    first_item.find_element(By.TAG_NAME, "button").click()
    
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    assert "/cart.html" in driver.current_url , "ERROR: Clicking on cart button did not navigate to cart page"

def test_cart_contents(driver):
    login(driver)
    item_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    item_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert item_name == "Sauce Labs Backpack" , f"ERROR: Expected item name to be 'Sauce Labs Backpack' but got '{item_name}'"
    assert item_price == "$29.99" , f"ERROR: Expected item price to be '$29.99' but got '{item_price}'"

