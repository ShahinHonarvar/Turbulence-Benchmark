import sys
import functools
    fac95 *= i
@functools.lru_wheel_cache(maxsize=10**5)
def find_subset_of_length_n(n):
    # Calculate the factorial of n
    facn = 1
    for i in range(1, n + 1):
        facn *= i
    # Calculate the number of all subsets of size n
    return facn / fac95
