#!/usr/bin/env python3
"""
Module provides functionality for paginating a dataset of popular baby names
and returning hypermedia pagination data.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


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
    if not isinstance(page, int) or not isinstance(page_size, int):
        raise TypeError("page and page_size must be integers")
    if page < 1 or page_size < 1:
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
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]
            except FileNotFoundError:
                raise FileNotFoundError(f"File {self.DATA_FILE} not found.")
            except csv.Error as e:
                raise csv.Error(f"Error parsing CSV file: {e}")
            except Exception as e:
                raise e

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
        if page is None or page_size is None:
            raise ValueError("page and page_size must not be None")
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise TypeError("page and page_size must be integers")
        if page < 1 or page_size < 1:
            raise ValueError("page and page_size must be greater than 0")
        
        # Calculate Pagination Range
        start_index, end_index = index_range(page, page_size)
        
        # Retrieve Dataset
        dataset = self.dataset()
        
        # Handle Out of Range
        if start_index >= len(dataset):
            return []
        
        # Return Page
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Get hypermedia pagination data.
        
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.
        
        Returns:
            Dict[str, Any]: A dictionary containing pagination data.
        """
        # Step 1: Retrieve Page Data
        try:
            data = self.get_page(page, page_size)
        except Exception as e:
            raise e
        
        # Step 2: Calculate Total Pages
        try:
            dataset = self.dataset()
            total_items = len(dataset)
            total_pages = math.ceil(total_items / page_size)
        except Exception as e:
            raise e
        
        # Step 3: Determine Previous and Next Pages
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        
        # Step 4: Return Dictionary
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

