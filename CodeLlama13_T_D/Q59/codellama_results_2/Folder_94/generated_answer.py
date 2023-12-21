
def all_left_truncatable_prime(numbers):
    left_truncatable_primes = []
    for n in numbers:
        if n > 1 and is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)

def is_left_truncatable_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
