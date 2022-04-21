import argparse

from crawler import Crawler


if __name__ == "__main__":
    args = argparse.ArgumentParser(description='Start service')
    args.add_argument('-u', '--url', type=str, help='URL do mangá', required=True)
    args.add_argument('-p', '--download_path', type=str, help='Path onde será baixado', required=False)
    args.add_argument('-d', '--debug', help='Modo visual', action="store_true", default=False)

    params = args.parse_args()
    url = params.url
    download_path = params.download_path
    debug = params.debug

    crawler = Crawler(url=url, download_path=download_path, debug=debug)
    crawler.start()
