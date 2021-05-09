from pathlib import Path
from typing import List
from bs4 import BeautifulSoup
from download.data_filter import DataFilter
from download.download_configuration import DownloadConfiguration, DateRange
from download.downloader import Downloader
import concurrent.futures

import requests

BASE_URL = "https://bulkdata.uspto.gov/"

page = requests.get(BASE_URL)
html = page.content

soup = BeautifulSoup(html, "html.parser")

# redbook is the pattern to match!s
# https://bulkdata.uspto.gov/data/patent/grant/redbook/2021
# https://bulkdata.uspto.gov/data/patent/grant/redbook/2021/I20210105.tar

date_range = DateRange(start=2021, end=2021)
conf = DownloadConfiguration(Path("tarfiles"), date_range)
df = DataFilter(conf)
a = df.get_redbook_data(soup=soup)
b = df.filter_by_year(a)
c = df.get_all_download_urls(b)
print(c)
urls: List[str] = c

downloader = Downloader(config=conf, d_filter=df)
print(f"Number of URLS: {len(urls)}")
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(downloader.download_tar, urls)
