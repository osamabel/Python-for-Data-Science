import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. "
}


def encode_to_morse(text: str) -> str:
    """
    Encode a string into Morse code.
    
    Args:
        text: Input string containing alphanumeric characters and spaces
        
    Returns:
        Morse code representation of the input string
        
    Raises:
        ValueError: If text contains unsupported characters
    """
    result = []
    for char in text:
        if char not in NESTED_MORSE:
            raise ValueError(f"Unsupported character: {char}")
        result.append(NESTED_MORSE[char])
    
    # Join and remove trailing space
    return ''.join(result).rstrip()


def validate_input(text: str) -> bool:
    """
    Validate that input contains only supported characters.
    
    Args:
        text: Input string to validate
        
    Returns:
        True if all characters are supported, False otherwise
    """
    for char in text:
        if char not in NESTED_MORSE:
            return False
    return True


def main() -> None:
    """
    Main function that handles command-line arguments and encodes text to Morse code.
    
    Handles error cases:
    - Wrong number of arguments
    - Wrong argument type
    - Unsupported characters in input
    """
    try:
        # Check number of arguments
        if len(sys.argv) != 2:
            print("AssertionError: the arguments are bad")
            return
        
        # Get input text and convert to uppercase
        text = sys.argv[1].upper()
        
        # Check if input is a valid string
        if not isinstance(sys.argv[1], str):
            print("AssertionError: the arguments are bad")
            return
        
        # Validate input contains only supported characters
        if not validate_input(text):
            print("AssertionError: the arguments are bad")
            return
        
        # Encode to Morse code
        morse_code = encode_to_morse(text)
        print(morse_code)
        
    except Exception as e:
        print("AssertionError: the arguments are bad")
        return


if __name__ == "__main__":
    main()
