
def all_left_truncatable_prime(tuple):
    x = tuple[8]
    primes = []
    for i in range(1, int(x**0.5) + 1):
        if i % 2 == 0 and i != 2:
            continue
        for j in range(1, int((x - 1) / (i * i)) + 1):
            n = i * i + j * j
            if is_left_truncatable_prime(n):
                primes.append(n)
    return sorted(primes, reverse=True)

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n % 10):
            return False
        n //= 10
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
