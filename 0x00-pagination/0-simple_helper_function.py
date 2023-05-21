#!/usr/bin/python3
""" This is an helper function that helps get index_range """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ This function gets the range of index used to paginate """
    start_index = page_size * (page - 1)
    end_index = page * page_size
    return (start_index, end_index)
