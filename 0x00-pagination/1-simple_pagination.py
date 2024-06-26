#!/usr/bin/env python3
"""
Module provides functionality for paginating a dataset of popular baby names.
"""

import csv
from typing import List, Tuple


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
        raise ValueError("page and page_size must not be None")
    if page <= 0 or page_size <= 0:
        raise ValueError("page and page_size must be greater than 0")
    start_index = (page - 1) * page_size
    end_index = page * page_size
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
        """Get a page from the dataset.
        
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.
        
        Returns:
            List[List]: A list of rows for the requested page.
        """
        # Assertions
        assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0"
        
        # Calculate Pagination Range
        start_index, end_index = index_range(page, page_size)
        
        # Retrieve Dataset
        dataset = self.dataset()

        # Handle Out of Range
        if start_index >= len(dataset) or end_index > len(dataset):
            return []

        # Return Page
        return dataset[start_index:end_index]

