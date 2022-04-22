import os

from driver.chromium import Chromium


class Crawler:

    def __init__(self, url: str, download_path: str, debug: bool):
        self.url = url
        self.download_path = download_path
        if not self.download_path:
            current_path = os.path.abspath(os.getcwd())
            manga_name = url.split("/")[4]
            self.download_path = os.path.join(current_path, manga_name)
            os.makedirs(self.download_path, exist_ok=True)

        self.download_path = download_path
        self.debug = debug

    def start(self):
        with Chromium(debug=self.debug) as chromium:
            driver = chromium.driver
            driver.get(self.url)
