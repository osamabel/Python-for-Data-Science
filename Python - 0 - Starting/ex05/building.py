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


def display_results(text: str, counts: dict) -> None:
    """
    Display the character count results.

    Args:
        text: The original text
        counts: Dictionary with character counts
    """
    print(f"The text contains {len(text)} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def get_text_from_stdin() -> str:
    """
    Get text input from stdin (can handle multiple lines).

    Returns:
        The input text as a string
    """
    print("What is the text to count?")
    try:
        lines = []
        while True:
            line = sys.stdin.readline()
            if not line:  # EOF (Ctrl+D)
                break
            lines.append(line)
        # Don't strip to keep the newline character
        text = ''.join(lines)
        # Remove only trailing whitespace except newlines
        return text.rstrip(' \t')
    except EOFError:
        text = ''.join(lines) if lines else ""
        return text.rstrip(' \t') if text else ""


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
            print("AssertionError: more than one argument is provided")
            return
        elif len(sys.argv) == 2:
            # Use the provided argument
            text = sys.argv[1]
        else:
            # No argument provided, prompt for input
            text = get_text_from_stdin()

        # Process and display results
        counts = count_characters(text)
        display_results(text, counts)

    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main()
