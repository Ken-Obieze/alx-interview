#!/usr/bin/python3
"""Module define isWinner fuction for Prime Game."""


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if not nums or x < 1:
        return None

    wins = {'Maria': 0, 'Ben': 0}

    for n in nums:
        primes = sum([is_prime(i) for i in range(n + 1)])
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
