def all_right_truncatable_prime(n):
    # sort the primes less than the given number
    primes = sorted(range(2, n[0] + 1), key=lambda x: -is_prime(x))
    # return the right-truncatable primes in the list
    return [p for p in primes if is_right_truncatable_prime(p)]
def is_prime(n):
    # if the number is 0 or 1, it is not prime
    if n <= 1:
        return False
    # if the number is even, it is not prime
    if n % 2 == 0:
        return False
    # if the number is divisible by any of the primes from 2 to sqrt(n), it is not prime
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    # if none of the above tests failed, the number is prime
    return True
def is_right_truncatable_prime(n):
    # if the number is 0 or 1, it is not prime
    if n <= 1:
        return False
    # if the number is even, it is not prime
    if n % 2 == 0:
        return False
    # if the number is divisible by any of the primes from 2 to sqrt(n), it is not prime
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    # if none of the above tests failed, the number is prime
    return True
