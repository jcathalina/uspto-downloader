import requests
import logging
import logging.config
import yaml
from bs4 import BeautifulSoup

from download_configuration import DownloadConfiguration

with open("configuration/log_config.yaml") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config=config)

logger = logging.getLogger(__name__)


class Downloader:
    def __init__(self, download_config: DownloadConfiguration):
        self.download_config = download_config

    def download(self):
        pass



