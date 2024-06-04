from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.login import LoginPage

def test_first(driver):
    
   
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(2)

    # Get page title
    title = driver.title

    # Test if title is correct
    assert "Swag Labs" in title
    
def test_login(driver):
    
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(2)
    # Find element using element's id attribute
    # driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # driver.find_element(By.ID, "password").send_keys("secret_sauce")
    login_page = LoginPage(driver)
    login_page.setUserName("standard_user")
    login_page.setPassword("secret_sauce")
    driver.implicitly_wait(2)
    # driver.find_element(By.ID, "login-button").click()
    login_page.clickLogin()
    driver.implicitly_wait(2)
    text = driver.find_element(By.CLASS_NAME, "title").text
     # Check if login was successful 
    assert "products" in text.lower()
    pass
def test_add_to_cart(driver):
        print("testing add to cart")
        test_login(driver)
        add_to_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")

        # Click three buttons to make the cart_value 3
        for btns in add_to_cart_btns[:3]:
            btns.click()
        cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert "3" in cart_value.text
        print("TEST PASSED : ADD TO CART", "\n")
        
def test_remove_from_cart(driver):
    print("testing remove from cart")
    test_add_to_cart(driver)
    remove_from_cart_btns = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    # Click three buttons to make the cart_value 3
    for btns in remove_from_cart_btns[:2]:
        btns.click()
    cart_value = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert "1" in cart_value.text
    print("TEST PASSED : REMOVE FROM CART", "\n")