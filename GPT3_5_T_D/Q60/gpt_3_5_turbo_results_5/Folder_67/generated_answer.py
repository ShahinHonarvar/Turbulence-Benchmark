
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 10:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 10:
        n = int(str(n)[:-1])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[71]
    truncatable_primes = []
    for i in range(x, 9, -1):
        if '0' not in str(i) and is_left_truncatable_prime(i) and is_right_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
