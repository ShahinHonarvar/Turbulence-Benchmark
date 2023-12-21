import math
def all_right_truncatable_prime(n):
    # Find primes less than x
    primes = []
    for num in range(2, int(math.ceil(math.sqrt(n[0])) + 1):
        is_prime = True
        # Check if prime
        for i in range(num):
            if num % 10 ** (i + 1) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    # Filter for right-truncatable primes
    right_truncatable_primes = []
    for prime in primes:
        # Check if prime after removing rightmost digit
        for i in range(9):
            if str(prime)[:-1] % 10 ** (i + 1) == 0:
                break
            else:
                right_truncatable_primes.append(prime)
    # Sort in descending order
    return sorted(right_truncatable_primes, reverse=True)
