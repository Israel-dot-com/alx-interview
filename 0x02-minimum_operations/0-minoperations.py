#!/usr/bin/python3
'''Min Operation Interview Problem'''


def minOperations(n):
    ''' Finds the Miinimum Operation
    required
    '''
    if n <= 1:
        return 0
    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n /= i
        i += 1
    return operations
