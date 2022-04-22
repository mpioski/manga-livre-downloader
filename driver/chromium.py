import undetected_chromedriver as uc
from selenium import webdriver

from driver.abstract import Abstract


class Chromium(Abstract):

    def __init__(self, debug=False):
        self.options = webdriver.ChromeOptions()
        if not debug:
            self.options.add_argument("--headless")

    def __enter__(self):
        self.__instance_driver()
        return self

    def __instance_driver(self):
        self.driver = uc.Chrome(options=self.options)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
