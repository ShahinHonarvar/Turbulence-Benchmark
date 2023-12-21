
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for x in numbers:
        if is_left_truncatable_prime(x):
            left_truncatable_primes.append(x)
    return sorted(left_truncatable_primes)

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(1, int(len(str(n)) / 2)):
        if not is_prime(n):
            return False
        n //= 10
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
