def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.

    Args:
        function: A function that takes one argument and returns
            True/False, or None
        iterable: An iterable object to filter

    Returns:
        A list containing items for which function returns True,
        or items that are truthy if function is None
    """
    if function is None:
        # Return items that are truthy
        return [item for item in iterable if item]
    else:
        # Return items for which function returns True
        return [item for item in iterable if function(item)]
