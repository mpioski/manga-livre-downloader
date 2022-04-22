import os
import requests

from driver.chromium import Chromium
from selenium.webdriver.common.by import By


class Crawler:

    def __init__(self, url: str, download_path: str, debug: bool):
        self.url = url
        self.download_path = download_path
        if not self.download_path:
            current_path = os.path.abspath(os.getcwd())
            manga_name = url.split("/")[4]
            download_path = os.path.join(current_path, manga_name)
            os.makedirs(download_path, exist_ok=True)

        self.download_path = download_path
        self.debug = debug
        self.chromium = None

    def start(self):
        with Chromium(debug=self.debug) as chromium:
            self.chromium = chromium
            self.chromium.driver.get(self.url)

            total_pages = self.get_total_pages()
            for current_page in range(int(total_pages)):
                self.download_page(current_page)
                next_page = self.get_next_page(page=current_page)
                self.chromium.driver.get(next_page)
                self.chromium.driver.refresh()

    def get_total_pages(self):
        print("Capturando total de páginas")
        page_navigation = self.chromium.driver.find_element(by=By.CLASS_NAME, value="page-navigation")
        total_pages = page_navigation.find_elements(by=By.TAG_NAME, value="em")[1].text
        print("Encontrados {} páginas".format(total_pages))
        return total_pages

    def download_page(self, page: int):
        print("Realizando download da página {}".format(page + 1))

        manga_image = self.chromium.wait_until_class_name(element=self.chromium.driver, class_name="manga-image")
        img = self.chromium.wait_unitl_tag_name(element=manga_image, tag_name="img")
        image_link = img.get_attribute("src")
        data = requests.get(image_link).content
        with open(f"{self.download_path}/{page}.png", 'wb') as f:
            f.write(data)

        print("Download concluído")

    def get_next_page(self, page: int):
        page = "#/!page{0}".format(str(page + 1))
        return self.url + page
