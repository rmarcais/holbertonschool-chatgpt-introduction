#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given integer n using recursion.

    Parameters:
    n (int): The integer for which to calculate the factorial.

    Returns:
    int: The factorial of n. Returns 1 if n is 0 (base case).

    Description:
    The function multiplies n by the factorial of (n-1) recursively until n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
