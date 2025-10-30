# Python-for-Data-Science

## PYTHON - 0
### EX00 - Mutable vs Immutable Objects

>> ### Key Concepts:
>> - **Mutable objects** (List, Set, Dictionary): Can be modified in place after creation
>> - **Immutable objects** (Tuple): Cannot be modified; must create new object to change values
>> ### Python Data Structures:
>> 1. **List** `[]` - Ordered, mutable collection
>> 2. **Tuple** `()` - Ordered, immutable collection
>> 3. **Set** `{}` - Unordered, mutable collection of unique elements
>> 4. **Dictionary** `{}` - Unordered collection of key-value pairs
>> ### Lesson:
>> Understanding mutability is crucial for data manipulation, memory efficiency, and data integrity in Python programming and data science.


### EX01 - Date and Time Formatting

>> ### Key Concepts:
>> - **Unix Epoch**: January 1, 1970 - the reference point for Unix timestamps
>> - **Timestamp**: Number of seconds elapsed since the Unix epoch
>> - **Date Formatting**: Using `strftime()` to format dates in specific patterns
>> ### Python Libraries:
>> - `datetime` module for date and time operations
>> - `strftime()` for formatting dates (e.g., "%b %d %Y" → "Oct 21 2022")
>> - `timestamp()` to get seconds since Unix epoch
>> ### F-String Formatting:
>> - `:,.4f` - Comma separator + 4 decimal places (e.g., `1,234,567.1235`)
>> - `:.2e` - Scientific notation with 2 decimals (e.g., `1.23e+06`)
>> 
>> | Code | Name | Example | Output |
>> |------|------|---------|--------|
>> | `f` | Fixed-point | `f"{123.456:.2f}"` | `123.46` |
>> | `e` | Scientific | `f"{1234:.2e}"` | `1.23e+03` |
>> | `%` | Percentage | `f"{0.1234:.2%}"` | `12.34%` |
>> | `d` | Decimal | `f"{1234:d}"` | `1234` |
>> ### Breakdown
>> `:` - starts the format specification
>> `,` - adds thousand separators (commas)
>> `.4` - specifies 4 decimal places
>> `f` - fixed-point notation (decimal format)
>> ### Lesson:
>> Understanding date/time manipulation is essential for data science tasks like time series analysis, data logging, and temporal data processing.


### EX02 - Type Checking and Function Returns

>> ### Key Concepts:
>> - **Type introspection**: Using `type()` to identify object types at runtime
>> - **Type names**: Accessing type names with `type().__name__`
>> - **Function returns**: Functions can return values while performing side effects (printing)
>> ### Python Techniques:
>> - `type(object)` - Returns the type of an object
>> - `type().__name__` - Gets the string name of the type
>> - Conditional logic based on type checking
>> - Return values in functions
>> ### Lesson:
>> Type checking is fundamental for data validation, error handling, and creating flexible functions that handle different data types appropriately.


### EX03 - Detecting "Null-like" Values

>> ### Key Concepts:
>> - **Falsy values**: Different representations of "null" or "empty" in Python
>> - **Type checking order**: Checking `bool` before `int` (since `False == 0` is `True`)
>> - **NaN detection**: Using `math.isnan()` to identify Not-a-Number floats
>> - **Return codes**: Using 0 for success, 1 for error
>> ### Python "Null" Values:
>> - `None` - The true null value
>> - `float("NaN")` - Not a Number (mathematical undefined)
>> - `0` - Zero integer
>> - `""` - Empty string
>> - `False` - Boolean false
>> ### Important:
>> - `False == 0` returns `True` in Python!
>> - Always check `bool` type before `int` when both could be 0
>> - Use `is None` not `== None` for identity check
>> ### Lesson:
>> Understanding Python's truthiness and falsy values is crucial for data validation, especially when cleaning datasets with missing or null values in data science.


### EX04 - Command-Line Arguments and Input Validation

>> ### Key Concepts:
>> - **Command-line arguments**: Using `sys.argv` to handle CLI input
>> - **Input validation**: Checking argument count and type
>> - **Error handling**: Using try-except for graceful error messages
>> - **Modulo operator**: Using `%` to check even/odd numbers
>> ### Python Techniques:
>> - `sys.argv` - List of command-line arguments
>> - `len(sys.argv)` - Count arguments
>> - `int()` conversion with error handling
>> - `if __name__ == "__main__"` pattern
>> ### Mathematical Concept:
>> - Even number: `number % 2 == 0`
>> - Odd number: `number % 2 != 0`
>> - Zero is considered even!
>> ### Lesson:
>> Command-line interface programming and input validation are essential skills for building robust scripts and tools in data science pipelines.


### EX05 - Character Counting and String Analysis

>> ### Key Concepts:
>> - **String manipulation**: Iterating and analyzing character types in strings
>> - **Character classification**: Using string methods to identify character types
>> - **Interactive input**: Reading from stdin when no arguments provided
>> - **Program structure**: Proper use of functions, main, and exception handling
>> ### Python Techniques:
>> - `string.punctuation` - Built-in punctuation characters
>> - `.isupper()`, `.islower()`, `.isdigit()`, `.isspace()` - Character type checks
>> - `sys.stdin.readline()` - Reading line by line from stdin
>> - Function documentation with docstrings
>> ### Best Practices:
>> - No code in global scope (all code in functions)
>> - Every program must have a `main()` function
>> - Use `if __name__ == "__main__":` pattern
>> - Catch all exceptions with try-except blocks
>> - All functions must have documentation (__doc__)
>> ### Accessing Documentation:
>> - `function.__doc__` - Get docstring as string
>> - `help(function)` - Show formatted help for function
>> - `help(module)` - Show help for entire module
>> - In IPython: `function?` shows docstring, `function??` shows source
>> ### Lesson:
>> Proper program structure, error handling, and string analysis are fundamental skills for data processing, text analysis, and building robust command-line tools in data science.


### EX06 - Filter Function and List Comprehensions

>> ### Key Concepts:
>> - **Functional programming**: Implementing higher-order functions
>> - **List comprehensions**: Concise way to create and filter lists
>> - **Lambda functions**: Anonymous functions for inline operations
>> - **Filtering logic**: Selecting elements based on conditions
>> ### Python Techniques:
>> - List comprehension syntax: `[item for item in iterable if condition]`
>> - Lambda functions: `lambda x: condition`
>> - Built-in `filter()` function behavior
>> - String operations: `.split()`, `len()`
>> ### Iterators and Filter:
>> - **Built-in `filter()`** returns an **iterator object**, not a list
>> - **Iterator protocol**: Requires `__iter__()` and `__next__()` methods
>> - `iter(filter_obj)` returns the iterator itself
>> - `next(filter_obj)` yields the next filtered item or raises StopIteration
>> - **Memory efficient**: Lazy evaluation - only computes when accessed
>> - Convert to list: `list(filter(...))` to get all results at once
>> ### Important:
>> - List comprehensions are more Pythonic than loops
>> - Lambdas are useful for simple, inline operations
>> - Filter returns items where function returns True
>> - If function is None, filter returns truthy items
>> - Our `ft_filter` returns a list (eager), built-in returns iterator (lazy)
>> ### Lesson:
>> Understanding functional programming concepts like filtering and using list comprehensions makes data manipulation more efficient and readable in data science workflows.
