import itertools
def all_right_truncatable_prime(n):
    # Create a list of prime numbers less than n
    primes = [x for x in range(2, n) if all(x % d != 0 for d in range(3, int(x ** .5) + 1, 2))]
    # Create a list of all right-truncatable prime numbers less than n
    right_truncatable_primes = []
    for p in primes:
        # Remove the last right-most digit from p and check if it is still prime
        if p % 10:
            for d in range(1, 10):
                if p % d == 0:
                    break
                elif d == 10:
                    # The number is no longer prime, so break out of the loop
                    break
                elif p // d * d == p:
                    # The number is still prime, so add it to the list of right-truncatable primes
                    right_truncatable_primes.append(p)
                    break
    # Sort the list of right-truncatable primes and return it
    return sorted(right_truncatable_primes)
