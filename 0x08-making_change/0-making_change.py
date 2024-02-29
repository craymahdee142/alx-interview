#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    # if the total is zero or less, we don't need any coin
    if total <= 0:
        return 0

    # Sort the coins in desecnding order to try the largest dominates first
    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        if coin > total:
            # If the coin value is larger than the remaining total, s
            continue

        # Calculate how many coins of this denomination can be used
        count = total // coin

        # Reduce the remaining total by the amount covered by these coins
        total -= count * coin

        coin_count += count

        # If the total is now 0, break out of the loop as we have the
        if total == 0:
            break

    # If we have exited the loop but still have a remaining total, return -1
    if total > 0:
        return -1

    # Otherwise return total  umber of coins
    return coin_count
