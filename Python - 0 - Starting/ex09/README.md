# ft_package

A sample test package for Python.

## Installation

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```

## Functions

### count_in_list(lst, item)

Counts the number of occurrences of an item in a list.

**Parameters:**
- `lst` (list): The list to search in
- `item`: The item to count

**Returns:**
- `int`: The number of occurrences

## License

MIT License - see LICENSE file for details

