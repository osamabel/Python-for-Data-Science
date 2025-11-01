import sys
from ft_filter import ft_filter


def main() -> None:
    """
    Main function that handles command-line arguments and filters words.

    Takes two command-line arguments:
    - sentence: A string containing words separated by spaces
    - n: An integer representing the minimum length threshold

    Filters words from the sentence that have length greater than n
    using ft_filter.

    Handles error cases:
    - Wrong number of arguments
    - Wrong argument types (n must be an integer)
    """
    try:
        # Check number of arguments
        if len(sys.argv) != 3:
            print("AssertionError: the arguments are bad")
            return

        # Parse arguments
        sentence = sys.argv[1]
        words = sentence.split()
        try:
            n = int(sys.argv[2])
        except ValueError:
            print("AssertionError: the arguments are bad")
            return

        # Filter words with length greater than n using ft_filter
        result = list(ft_filter(lambda word: len(word) > n, words))
        print(result)

    except Exception:
        print("AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()
