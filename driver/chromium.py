import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium import webdriver

from driver.abstract import Abstract


class Chromium(Abstract):

    def __init__(self, debug=False):
        self.options = webdriver.ChromeOptions()
        ua = UserAgent()
        user_agent = ua.random
        self.options.add_argument(f'user-agent={user_agent}')

        if not debug:
            self.options.add_argument("--headless")

    def __enter__(self):
        self.__instance_driver()
        return self

    def __instance_driver(self):
        print("Instanciando driver do chrome")
        self.driver = uc.Chrome(options=self.options)
        self.driver.implicitly_wait(10)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
