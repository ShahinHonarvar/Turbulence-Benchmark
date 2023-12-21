
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(1, x+1):
        if is_left_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)

def is_left_right_truncatable_prime(n):
    if n < 10:
        return False
    while len(str(n)) > 2:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
