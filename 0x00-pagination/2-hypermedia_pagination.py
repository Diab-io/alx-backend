#!/usr/bin/env python3
""" A server class that implements a simple pagination """
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range used for paginating.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This is used to get the page contents"""
        assert type(page_size) == int and type(page) == int
        assert page_size > 0 and page > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start > len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ This returns a dict with some hypermedia data  """
        data_set = self.get_page(page, page_size)
        data_page_size = len(data_set)
        data = data_set
        next_page = (page + 1) if len(data) > 0 else None
        prev_page = None if (page - 1) < 1 else page - 1
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': data_page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
