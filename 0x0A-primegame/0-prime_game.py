#!/usr/bin/python3
"""A function that determines who the winner of each game"""


def isWinner(x, nums):
    """Reurns the winner of each game"""
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    maria_wins, ben_wins = 0, 0

    for n in nums:
        is_removed = [False] * (n + 1)
        move_count = 0

        for prime in range(2, n + 1):
            if primes[prime] and not is_removed[prime]:
                for multiple in range(prime, n + 1, prime):
                    is_removed[multiple] = True
                move_count += 1

        if move_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
