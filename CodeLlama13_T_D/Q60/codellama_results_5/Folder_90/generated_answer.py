
def all_left_right_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if is_prime(n) and no_zeroes(n):
            primes.append(n)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def no_zeroes(n):
    while n > 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True
