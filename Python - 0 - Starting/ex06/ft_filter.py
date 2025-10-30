import sys


def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    
    Args:
        function: A function that takes one argument and returns True/False, or None
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


def main() -> None:
    """
    Main function to test ft_filter implementation.
    
    Tests the custom filter function with various inputs to ensure
    it behaves like the built-in filter function.
    """
    try:
        print("=== Testing ft_filter with numbers ===")
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # Filter even numbers
        even_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
        print(f"Even numbers: {even_numbers}")
        
        # Filter numbers greater than 5
        greater_than_5 = ft_filter(lambda x: x > 5, numbers)
        print(f"Numbers > 5: {greater_than_5}")
        
        # Filter truthy values (function is None)
        truthy_values = ft_filter(None, [0, 1, '', 'hello', False, True, None, 42])
        print(f"Truthy values: {truthy_values}")
        
        print("\n=== Testing ft_filter with strings ===")
        words = ['hello', 'world', 'test', '', 'python', '42', '']
        
        # Filter non-empty strings
        non_empty = ft_filter(lambda x: len(x) > 0, words)
        print(f"Non-empty strings: {non_empty}")
        
        # Filter strings longer than 4 characters
        long_words = ft_filter(lambda x: len(x) > 4, words)
        print(f"Long words: {long_words}")
        
        # Filter truthy strings (function is None)
        truthy_strings = ft_filter(None, words)
        print(f"Truthy strings: {truthy_strings}")
        
        print("\n=== Comparison with built-in filter ===")
        test_list = [1, 0, 3, '', 'hello', None, 42, False, True]
        
        custom_result = ft_filter(lambda x: isinstance(x, int) and x > 0, test_list)
        builtin_result = list(filter(lambda x: isinstance(x, int) and x > 0, test_list))
        print(f"Custom filter: {custom_result}")
        print(f"Built-in filter: {builtin_result}")
        print(f"Results match: {custom_result == builtin_result}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main()
