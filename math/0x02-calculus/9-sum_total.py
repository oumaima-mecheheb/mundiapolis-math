#!/usr/bin/env python3


def summation_i_squared(n):
    '''
    Calculates the sum of i to the power of 2 from i equals 1 to n.
    '''

    if not isinstance(n, int) or n <= 0:
        return None
    return int((n*(n + 1)*(2*n + 1)) / 6)

summation_i_squared = __import__('9-sum_total').summation_i_squared

n = 5
print(summation_i_squared(n))