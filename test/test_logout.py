import time

from selenium.webdriver.common.by import By

from pages.inventory import Inventory
import pytest
import time
@pytest.mark.skip
@pytest.mark.order(2)
@pytest.mark.sanity
#@pytest.mark.dependency(depends=["add_product"], name="checkout_confirm")
def test_logout(driver,login):
    assert True