from driver.chromium import Chromium


class Crawler:
    def __init__(self, url: str, download_path: str, debug: bool):
        self.url = url
        self.download_path = download_path
        self.debug = debug

    def start(self):
        with Chromium(debug=self.debug) as driver:
            driver.get(self.url)

