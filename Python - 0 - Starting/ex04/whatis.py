import sys

# Check number of arguments
if len(sys.argv) > 2:
    # More than one argument
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 2:
    # Try to convert to integer
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
    else:
        # Check if odd or even
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
