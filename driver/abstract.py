from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Abstract:

    @staticmethod
    def wait_until_class_name(element, class_name, timeout=60):
        return WebDriverWait(element, timeout).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, class_name))
        )

    @staticmethod
    def wait_unitl_tag_name(element, tag_name, timeout=60):
        return WebDriverWait(element, timeout).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, tag_name))
        )
