import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.inventory import Inventory
import pytest
import time

@pytest.mark.order(3)
#@pytest.mark.dependency(depends=["checkout_confirm"])
@pytest.mark.smoke
def test_checkout_cencel(driver,login):
        inventory = Inventory(driver)

        inventory.add_cart("Sauce Labs Onesie")
        inventory.go_to_cart()
        inventory.checkout_cancel()


        assert "inventory" in driver.current_url
        time.sleep(5)