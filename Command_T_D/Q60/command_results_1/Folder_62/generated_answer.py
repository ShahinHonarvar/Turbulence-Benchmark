
import re
import sys
import math
import heapq

sys.setrecursionlimit(10**6)

# Use this function to create prime numbers from 2 to x
def prime_table(x):
    primes = []
    # Go through all numbers from 2 to x
    for i in range(2, x+1):
        # If the number is prime, add it to the list of primes
        if all(n % i for n in range(i**2, x+1, i)):
            primes.append(i)
    return primes

# Use this function to find all left-and-right-truncatable prime numbers less than or equal to x
def all_left_right_truncatable_prime(nums):
    # Create a list of all prime numbers less than or equal to the given number
    primes = prime_table(nums[0])
    # Sort the list of primes in ascending order
    primes.sort()
    # Create a list to store the left-and-right-truncatable prime numbers
    ltr_primes = []
    # Go through each prime in the list of primes
    for p in primes:
        # Create a list to store the left-and-right-truncatable prime numbers
        curr_ltr_primes = []
        # Go through each digit in the prime number
        for d in str(p):
            # If the digit is 0, then break out of the loop
            if d == '0':
                break
            # If the digit is 1 or 2, then continue with the next digit
            elif d == '1' or d == '2':
                continue
            # If the digit is not 1, 2, or 0, then break out of the loop
            else:
                break
        # If the list of curr_ltr_primes is empty, then break out of the loop
        if not curr_ltr_primes:
            break
        # Add the current left-and-right-truncatable prime number to the list
        ltr_primes.append(p)
    # Return the list of left-and-right-truncatable prime numbers
    return ltr_primes
