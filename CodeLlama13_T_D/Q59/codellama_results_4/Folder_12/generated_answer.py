
def all_left_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            primes.append(number)
    return sorted(primes, reverse=True)

def is_left_truncatable_prime(n):
    if n < 2 or '0' in str(n):
        return False
    for i in range(1, int(len(str(n)) / 2) + 1):
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
