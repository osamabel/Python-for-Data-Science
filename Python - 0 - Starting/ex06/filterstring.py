import sys


def filter_string(sentence: str, n: int) -> list:
    """
    Filter words from a sentence that have length greater than N.
    
    Args:
        sentence: Input string containing words separated by spaces
        n: Minimum length threshold
        
    Returns:
        List of words with length > n
    """
    # Split sentence into words
    words = sentence.split()
    
    # Use lambda function to filter words by length
    filter_func = lambda x: len(x) > n
    
    # Use list comprehension with lambda to filter words
    result = [word for word in words if filter_func(word)]
    
    return result


def main() -> None:
    """
    Main function that handles command-line arguments and filters words.
    
    Handles error cases:
    - Wrong number of arguments
    - Wrong argument types
    """
    try:
        # Check number of arguments
        if len(sys.argv) != 3:
            print("AssertionError: the arguments are bad")
            return
        
        # Parse arguments
        sentence = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            print("AssertionError: the arguments are bad")
            return
        
        # Filter words and print result
        result = filter_string(sentence, n)
        print(result)
        
    except Exception as e:
        print(f"AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()
