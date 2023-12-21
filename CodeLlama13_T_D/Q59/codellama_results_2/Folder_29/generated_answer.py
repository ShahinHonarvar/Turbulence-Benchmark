
def all_left_truncatable_prime(numbers):
    primes = []
    for n in numbers:
        if is_left_truncatable_prime(n):
            primes.append(n)
    return sorted(primes, reverse=True)

def is_left_truncatable_prime(n):
    if str(n).startswith('0'):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[i:])):
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
