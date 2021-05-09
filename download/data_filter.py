from typing import List

from download_configuration import DownloadConfiguration
from datetime import date
from bs4 import BeautifulSoup
import re


class DataFilter:
    def __init__(self, config: DownloadConfiguration):
        self.config = config

    @staticmethod
    def get_redbook_data(soup: BeautifulSoup) -> List[str]:
        """
        :return: relevant redbook data with full text + images
        """
        redbook_data = []
        for a_tag in soup.find_all('a', href=True):

            # the patents we are looking for include text + images
            # this corresponds to the URLs with redbook/YEAR pattern.
            if re.search(r"redbook/[0-9]", a_tag['href']):
                redbook_data.append(a_tag['href'])

        return redbook_data



    def filter_by_year(self, links: List[str]) -> List[str]:
        """
        :param links:
        :return:
        """
        filtered_links = []

        start = self.config.date_range.start
        end = self.config.date_range.end

        for link in links:
            year = int(link.rsplit('/', 1)[-1])
            if start <= year <= end:
                filtered_links.append(link)

        return filtered_links

    @staticmethod
    def get_tarfile_tags(soup: BeautifulSoup) -> List[str]:
        """
        :param soup: parsed html by BeautifulSoup
        :return: A list containing all the tags for each tar file on the page.
        """
        tarfile_tags = []
        for a_tag in soup.find_all('a', href=True):
            if 'tar' in a_tag.text:
                tarfile_tags.append(a_tag.text)
        return tarfile_tags
