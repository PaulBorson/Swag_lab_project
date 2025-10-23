import time

from selenium.webdriver.common.by import By

from pages.inventory import Inventory
import pytest
import time

@pytest.mark.order(2)
@pytest.mark.sanity
#@pytest.mark.dependency(depends=["add_product"], name="checkout_confirm")
def test_checkout_confirm(driver,login):
    inventory=Inventory(driver)
    inventory.add_cart("Sauce Labs Onesie")
    inventory.go_to_cart()
    inventory.checkout_confirm()

    thanks_msg=driver.find_element(By.CLASS_NAME,"complete-header").text

    assert "Thank " in thanks_msg,"Confirm !!!"

    time.sleep(2)