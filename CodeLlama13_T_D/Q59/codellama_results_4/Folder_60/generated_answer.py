
def all_left_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if is_prime(x) and no_leading_zeroes(x):
            primes.append(x)
    return sorted(primes)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def no_leading_zeroes(n):
    while n > 0 and n % 10 == 0:
        n //= 10
    return n != 0
