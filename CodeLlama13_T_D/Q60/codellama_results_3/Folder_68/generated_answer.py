
def all_left_right_truncatable_prime(x):
    left_truncatable_primes = []
    for i in range(1, x+1):
        if is_left_and_right_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
