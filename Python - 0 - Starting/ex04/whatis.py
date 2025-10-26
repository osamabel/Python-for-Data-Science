import sys

def check_odd_or_even():
    # Check number of arguments
    if len(sys.argv) == 1:
        # No arguments provided, do nothing
        return
    elif len(sys.argv) > 2:
        # More than one argument
        print("AssertionError: more than one argument is provided")
        return
    
    # Try to convert to integer
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    
    # Check if odd or even
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

check_odd_or_even()
