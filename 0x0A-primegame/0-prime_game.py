#!/usr/bin/python3
"""Module define isWinner fuction for Prime Game."""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.
    Args:
        x (int): The number of rounds to be played.
        nums (list of int): An array of n values for each round.
    Returns:
        str or None: The name of the player who won the most rounds.
    """


    def is_prime(n):
        """
        Check if a number is prime.
        Args:
            n (int): The number to check.
        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not nums or x < 1:
        return None

    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        primes = sum(1 for i in range(2, n + 1) if is_prime(i))
        if primes % 2 == 0:
            wins['Ben'] += 1
        else:
            wins['Maria'] += 1

    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None
