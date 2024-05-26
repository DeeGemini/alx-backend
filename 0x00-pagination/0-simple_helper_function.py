#!/usr/bin/env python3
"""
Module provides a function for calculating pagination range.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for a given page and page size.
    
    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.
    
    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index.
    """

    if page is None or page_size is None:
        raise ValueError("page and page_size cannot be None")
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be positive integers")
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
