from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path
from datetime import date


@dataclass
class DateRange:
    def __init__(self,
                 start: date.year = 1970,
                 end: date.year = date.today().year):
        self.start = start
        self.end = end


@dataclass
class DownloadConfiguration:
    def __init__(self, out_dir: Path, date_range: DateRange, async_dl: bool = False):
        self.out_dir = out_dir
        self.date_range = date_range
        self.async_dl = async_dl


