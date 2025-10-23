from selenium.webdriver.common.by import By

from pages.inventory import Inventory

import pytest
@pytest.mark.skip
@pytest.mark.order(4)
@pytest.mark.smoke
#@pytest.mark.dependency(name="add_product")
def test_add_product(driver,login):
    inventory = Inventory(driver)
    inventory.add_cart("abccegSauce Labs Bolt T-Shirt")
    inventory.add_cart("Test.allTheThings() T-Shirt (Red)")

    cartnum=driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cartnum == "2" ,"invalid cart number"
