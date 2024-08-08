#!/usr/bin/python3
"""A method that calculates the fewest number of operations
   needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """A function that calculates the number of operation."""
    if n <= 1:
        return 0

    ops = 0

    for x in range(2, n + 1):
        while n % x == 0:
            ops += x
            n //= x
        
        if n == 1:
            break
    
    return ops
