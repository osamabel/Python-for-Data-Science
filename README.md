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
