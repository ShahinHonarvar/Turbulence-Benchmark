
def all_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if is_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0 and not is_prime(i):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
