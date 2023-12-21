import itertools
import re
def all_left_truncatable_prime(n):
    # Left-truncatable primes less than x
    return sorted(set(itertools.permutations(str(n), 3)) + str(n))
    # Remove non-digit strings and invalid numbers
    .filter(lambda x: re.fullmatch(r"[a-zA-Z]+", x))
    # Check if each number is prime
    .filter(lambda x: all(x % i for i in range(2, int(x) // 2 + 1)))
