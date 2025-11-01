import sys
import string


def count_characters(text: str) -> dict:
    """
    Count different types of characters in a text.

    Args:
        text: The input string to analyze

    Returns:
        A dictionary containing counts of uppercase, lowercase, punctuation,
        digits, and spaces
    """
    counts = {
        'upper': 0,
        'lower': 0,
        'punctuation': 0,
        'spaces': 0,
        'digits': 0
    }

    for char in text:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
        elif char in string.punctuation:
            counts['punctuation'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        elif char.isdigit():
            counts['digits'] += 1

    return counts

def main() -> None:
    """
    Main function that handles command-line arguments and processes text.

    Handles error cases:
    - No arguments: prompts user for input
    - One argument: processes the argument
    - Multiple arguments: prints AssertionError
    """
    try:
        # Check number of arguments
        if len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        elif len(sys.argv) == 2:
            # Use the provided argument
            text = sys.argv[1]
        else:
            # No argument provided, prompt for input
            print("What is the text to count?")
            text = sys.stdin.readline()

        # Process and display results
        counts = count_characters(text)
        
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except Exception as e:
        print("AssertionError:", e)
        return


if __name__ == "__main__":
    main()
