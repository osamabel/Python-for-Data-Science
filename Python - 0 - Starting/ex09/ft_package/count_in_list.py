"""Module containing the count_in_list function."""


def count_in_list(lst: list, item) -> int:
    """
    Count occurrences of an item in a list.
    
    Args:
        lst: The list to search in
        item: The item to count
        
    Returns:
        The number of occurrences of item in lst
    """
    return lst.count(item)

