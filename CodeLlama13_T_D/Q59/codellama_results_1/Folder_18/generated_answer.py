
def all_left_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_prime(num) and not has_zero(str(num)):
            primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_zero(s):
    return '0' in s
