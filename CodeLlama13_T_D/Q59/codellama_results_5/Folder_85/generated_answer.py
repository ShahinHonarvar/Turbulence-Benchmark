
def all_left_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if is_left_truncatable_prime(x):
            primes.append(x)
    return sorted(primes)

def is_left_truncatable_prime(n):
    if n % 2 == 0 or n < 3:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
