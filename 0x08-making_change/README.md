# Making Change

This is a project that implements a function to calculate the fewest number of coins needed to meet a given amount total.

## Requirements

- General
  - Allowed editors: vi, vim, emacs
  - All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
  - All your files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/python3`
  - A README.md file, at the root of the folder of the project, is mandatory
  - Your code should use the PEP 8 style (version 1.7.x)
  - All your files must be executable

## Files

| Filename                 | Description                   |
| ------------------------ | ----------------------------- |
| [0-making_change.py](./0-making_change.py) | Python script that contains the implementation of the `makeChange` function |
| [0-main.py](./0-main.py) | Main file for testing the `makeChange` function |

## Usage

To test the `makeChange` function, you can run the `0-main.py` script. It contains sample test cases for the function.

```bash
./0-main.py
```

## Function Signature
The makeChange function is defined as follows:

```python
def makeChange(coins, total):
    pass
```

## Parameters
* coins: A list of the values of the coins in your possession.
* total: The target amount to be achieved.

## Return Value
The function returns the fewest number of coins needed to meet the total amount. It follows the following rules:
* If the total is 0 or less, it returns 0.
* If the total cannot be met by any number of coins you have, it returns -1.

## Example
Here's an example usage of the makeChange function:

```python
Copy code
print(makeChange([1, 2, 25], 37))
# Output: 7

print(makeChange([1256, 54, 48, 16, 102], 1453))
# Output: -1
```

## Author
Obieze, Ejiofor Kenneth
