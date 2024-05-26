#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            try:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:] if dataset else []
            except FileNotFoundError:
                print(f"Error: Could not find file {self.DATA_FILE}")
                self.__dataset = []

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            if dataset is None:
                raise ValueError("dataset is None")
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Get a page from the indexed dataset that is deletion-resilient.
        
        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items per page.
        
        Returns:
            Dict[str, Any]: A dictionary containing pagination data.
        """
        # Step 1: Assert Valid Index
        assert index is not None and 0 <= index < len(self.indexed_dataset()), "Invalid index"

        # Step 2: Initialize Data Structures
        dataset = self.indexed_dataset()
        
        # Step 3: Collect Data
        data = []
        current_position = index
        
        # Step 4: Populate Page Data
        while len(data) < page_size and current_position < len(dataset):
            if current_position in dataset:
                data.append(dataset[current_position])
            current_position += 1
        
        # Step 5: Determine Next Index
        next_index = current_position
        
        # Step 6: Return Dictionary
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }

