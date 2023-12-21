
def all_left_right_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if is_prime(n) and not contains_zero(str(n)):
            primes.append(n)
    return primes

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
