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
            raise AssertionError("the arguments are bad")

        # Parse arguments
        sentence = sys.argv[1]
        words = sentence.split()
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # Filter words with length greater than n using ft_filter
        result = list(ft_filter(lambda word: len(word) > n, words))
        print(result)

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
