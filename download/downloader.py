import requests
import logging
import logging.config
import yaml
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

from pathlib import Path
from download_configuration import DownloadConfiguration
from data_filter import DataFilter

with open("configuration/log_config.yaml") as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(config=log_config)

log = logging.getLogger(__name__)


class Downloader:
    def __init__(self,
                 config: DownloadConfiguration,
                 d_filter: DataFilter):
        self.config = config
        self.d_filter = d_filter


    def setup_out_dir(self):
        out_dir = self.config.out_dir
        if not Path.exists(out_dir):
            try:
                log.info(f"Creating directory {out_dir}")
                Path.mkdir(out_dir)
            except PermissionError as e:
                log.error(f"Can not create directory due to: {e}", exc_info=True)


    def download_tar(self, url: str):
        log.info(f"Downloading tar files @ {url}...")
        file_suffix = url.split("/")[-1]
        out_dir = self.config.out_dir
        filename = out_dir.joinpath(file_suffix)

        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            total_size = int(response.headers.get("content-length", 0))
            pbar = tqdm(total=total_size, desc=os.path.basename(filename), unit="B", unit_scale=True)
            with open(filename, "wb") as fileobj:
                for chunk in response.iter_content(chunk_size=1024):
                    fileobj.write(chunk)
                    pbar.update(len(chunk))
            pbar.close()
