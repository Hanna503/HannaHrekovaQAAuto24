import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.ui
def test_check_incorrect_username():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://github.com/login")

    login_elem = driver.find_element(By.ID, 'login_field')

    login_elem.send_keys('sergiibutenko@mistakeinemail.com')

    pass_elem = driver.find_element(By.ID, 'password')

    pass_elem.send_keys('wrong password')

    btn_elem = driver.find_element(By.NAME, 'commit')

    btn_elem.click()

    assert driver.title == 'Sign in to GitHub · GitHub'

    driver.close()


@pytest.mark.ui
def test_add_to_basket():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://rozetka.com.ua/ua/")

    try:
        popup_close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/a/span'))
        )
        popup_close_button.click()
    except:
        pass

    search_box = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/div/rz-search-suggest/form/div/div[1]/input'))
    )
    search_box.send_keys("холодильник")
    
    search_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/div/rz-search-suggest/form/button'))
    )
    search_button.click()

    try:
        popup_close_another_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/span/span'))
        )
        popup_close_another_button.click()
    except:
        pass

    first_item = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/rz-app-root/div/div/rz-category/div/main/rz-catalog/div/div/section/rz-grid/ul/li[1]/rz-catalog-tile/app-goods-tile-default/div/div[2]/div[1]/rz-button-product-page[1]/a'))
    )
    first_item.click()
    
    add_to_basket_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/rz-app-root/div/div/rz-product/div/rz-product-tab-main/div/div[1]/div[2]/div/rz-product-main-info/div/div[2]/div[1]/div[3]/rz-product-buy-btn/rz-buy-button/button'))
    )
    add_to_basket_button.click()
    
    remove_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cartProductActions0"]'))
    )
    remove_button.click()

    confirm_remove_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/rz-app-root/rz-single-modal-window/div[3]/div[2]/rz-shopping-cart/div/rz-cart-purchases/ul/li/rz-cart-product/div/div[1]/rz-popup-menu/div/ul/li[1]/rz-trash-icon/button'))
    )
    confirm_remove_button.click()
    
    empty_basket_message = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/rz-app-root/rz-single-modal-window/div[3]/div[1]/button'))
    )
    empty_basket_message.click()

    driver.close()


