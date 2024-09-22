#!/usr/bin/python3
"""A function that determines the fewest number
   of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins"""
    if total <= 0:
        return 0

    dynamic = [float('inf')] * (total + 1)
    dynamic[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dynamic[amount] = min(dynamic[amount],
                                      dynamic[amount - coin] + 1)

    return dynamic[total] if dynamic[total] != float('inf') else -1
