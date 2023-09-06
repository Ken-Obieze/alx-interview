# Prime Game

This is a Python program that simulates a prime number game played by Maria and Ben. The game involves choosing prime numbers from a set of consecutive integers starting from 1 up to a given number `n`. The players take turns removing a prime number and its multiples from the set. The player who cannot make a move loses the game.

The program determines the winner of each game based on a given number of rounds (`x`) and the values of `n` for each round. It assumes that Maria always goes first and both players play optimally.

## Requirements

- Python 3.4.3
- Ubuntu 14.04 LTS

## Usage

To run the program, use the following command:

```bash
./0-prime_game.py
```

Make the script executable by running:
```bash
chmod +x 0-prime_game.py
```

## Functionality
The program provides the isWinner(x, nums) function to determine the winner of the prime game. It takes the following parameters:

* `x:` The number of rounds to be played.
* `nums:` An array of n values for each round.
The function returns the name of the player who won the most rounds. If the winner cannot be determined, it returns None.

## Examples
```python
print(isWinner(5, [2, 5, 1, 4, 3]))
```
### Output:
```bash
Winner: Ben
```

## Author
Ejiofor Kenneth Obieze
