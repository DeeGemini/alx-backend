# Pagination Project

This project demonstrates various pagination techniques for handling large datasets, including deletion-resilient hypermedia pagination.

## Tasks

### Task 0: Simple Helper Function

**Objective**: Implement a helper function `index_range` that takes two integer arguments `page` and `page_size` and returns a tuple containing the start index and end index for the given pagination parameters.

**Function Signature**:
```python
def index_range(page: int, page_size: int) -> Tuple[int, int]:
Task 1: Simple Pagination
Objective: Create a Server class to paginate a dataset of popular baby names. Implement a get_page method that returns a specific page of the dataset based on page and page_size.

Class and Method:
class Server:
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

Task 2: Hypermedia Pagination
Objective: Extend the Server class with a get_hyper method that returns a dictionary with pagination metadata, including the current page, page size, dataset page, next page, previous page, and total pages.

Class and Method:
class Server:
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:

Task 3: Deletion-Resilient Hypermedia Pagination
Objective: Extend the Server class with a get_hyper_index method to handle pagination that is resilient to deletions in the dataset. This ensures that no items are missed when changing pages.

Class and Method:
class Server:
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:


Files
0-simple_helper_function.py: Contains the index_range function.
1-simple_pagination.py: Contains the Server class and get_page method.
2-hypermedia_pagination.py: Contains the Server class and get_hyper method.
3-deletion_resilient_pagination.py: Contains the Server class and get_hyper_index method.
Popular_Baby_Names.csv: The dataset used for pagination.

Requirements
All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
All files end with a new line.
The first line of all files is #!/usr/bin/env python3.
A README.md file is provided at the root of the project folder.
Code adheres to pycodestyle style (version 2.5.*).
File length is tested using wc.
All modules and functions have proper documentation.
All functions and coroutines are type-annotated.

