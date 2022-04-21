from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Abstract:

    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.timeout = timeout

    def wait_until_class_name(self, class_name: str):
        return WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name))
        )

    def wait_unitl_tag_name(self, tag_name: str):
        return WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, tag_name))
        )
