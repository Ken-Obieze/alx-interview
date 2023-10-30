# N Queens Solver

This program solves the N Queens problem, which involves placing N non-attacking queens on an N×N chessboard.

## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable

## Usage

The program should be invoked from the command line using the following syntax:

``` bash
./nqueens.py N
```

* If the user provides the wrong number of arguments, the program should print an error message "Usage: nqueens N" and exit with a status of 1.
* If N is not an integer, the program should print "N must be a number" and exit with a status of 1.
* If N is smaller than 4, the program should print "N must be at least 4" and exit with a status of 1.
* The program should print every possible solution to the N queens problem, one solution per line.

## Example
Here are examples of how to use the program:

```bash
./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## How to Run
To run the program, follow these steps:

* Clone the repository to your local machine.
* Navigate to the project directory.
* Execute the program with the appropriate command as described in the Usage section.

## File Structure
* 0-nqueens.py: The Python script that solves the N queens problem.
* README.md: This documentation file.

## PEP 8 Style
This project adheres to the PEP 8 style guidelines for Python code.
