import math
def all_left_truncatable_prime(n):
    # Write your code here
    # no-zero-left-truncatable-prime
    return [n for n in range(3, int(math.ceil(math.sqrt(n)) + 1) + 1) if is_left_truncatable_prime(str(n))]
    # is_left_truncatable_prime
    # Sieve of Eratosthenes
    # prime numbers
    # sort in descending order
