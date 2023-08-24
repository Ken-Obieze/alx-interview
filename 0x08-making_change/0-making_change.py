#!/usr/bin/python3
"""Module for Making change."""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    i = 0

    while total > 0 and i < len(coins):
        if coins[i] <= total:
            num_coins = total // coins[i]
            coin_count += num_coins
            total -= num_coins * coins[i]
        i += 1

    if total > 0:
        return -1

    return coin_count
