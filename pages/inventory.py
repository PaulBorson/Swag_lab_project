from selenium.webdriver.common.by import By
import time

class Inventory:
    def __init__(self, driver):
        self.driver = driver

    def add_cart(self, name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if product_name == name:
                product.find_element(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory").click()
                time.sleep(3)
                break


    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        f_name=self.driver.find_element(By.ID, "first-name").send_keys("prattoy")
        l_name=self.driver.find_element(By.ID, "last-name").send_keys("jackson")
        zip=self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID,'continue').click()

    def checkout_confirm(self):
        self.driver.find_element(By.ID, "finish").click()

    def checkout_cancel(self):
        self.driver.find_element(By.ID, "cancel").click()









