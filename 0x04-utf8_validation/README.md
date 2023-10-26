# UTF8 Validator

A Python function that determines if a given data set represents a valid UTF-8 encoding.

## Function Signature

```python:
def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
```

## Description
The validUTF8 function takes a list of integers, where each integer represents 1 byte of data, and checks if the data set represents a valid UTF-8 encoding. UTF-8 is a variable-length character encoding scheme where each character can be 1 to 4 bytes long.

The function iterates over each byte in the data set and performs the necessary checks to ensure it adheres to the UTF-8 encoding rules. It examines the leading byte to determine the number of bytes required to represent the current character and checks if the following bytes (if any) are valid continuation bytes. If an invalid byte or byte sequence is encountered, the function returns False. If all bytes are processed successfully and all characters are fully encoded, the function returns True.

## Usage
```python:
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
```
Replace data with your own list of integers representing the byte data that you want to check. The function will return True if the data set represents a valid UTF-8 encoding, and False otherwise.

Please note that the function assumes the given data set only contains the 8 least significant bits of each integer, as per the requirements.
