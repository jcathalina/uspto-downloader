from pathlib import Path
from typing import List
from bs4 import BeautifulSoup
from download.data_filter import DataFilter
from download.download_configuration import DownloadConfiguration, DateRange
from datetime import date

import requests
import dateparser

BASE_URL = "https://bulkdata.uspto.gov/"

page = requests.get(BASE_URL)
html = page.content

soup = BeautifulSoup(html, "html.parser")

# redbook is the pattern to match!s
# https://bulkdata.uspto.gov/data/patent/grant/redbook/2021
# https://bulkdata.uspto.gov/data/patent/grant/redbook/2021/I20210105.tar

date_range = DateRange(start=2005, end=2010)
conf = DownloadConfiguration(Path("."), date_range)
df = DataFilter(conf)
a = df.get_redbook_data(soup=soup)
b = df.filter_by_year(a)
print(b)
