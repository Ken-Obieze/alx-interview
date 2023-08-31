# Island Perimeter

This project contains a Python function `island_perimeter` that calculates the perimeter of an island described in a grid.

## Requirements

- Python version: 3.4.3
- Ubuntu version: 14.04 LTS

## Installation and Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/ken-obieze/alx-interview.git
   ```

2. Navigate to the project directory:
   ```shell
   cd alx-interview/0x09-island_perimeter
   ```

3. Run the main script:
   ```shell
   ./0-main.py
   ```
## Function Description
The `island_perimeter` function takes a grid representing an island and calculates its perimeter.

Syntax
```pythone
def island_perimeter(grid):
    """Calculate the perimeter of the island described in the grid.

    Args:
        grid (list): A list of lists representing the grid.

    Returns:
        int: The perimeter of the island.

    """
```

## Example
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```
## Constraints
* The grid is a rectangular list of lists with dimensions not exceeding 100.
* Each cell in the grid is either 0 (water) or 1 (land).
* The grid is completely surrounded by water.
* There is only one island (or nothing).
* The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).
