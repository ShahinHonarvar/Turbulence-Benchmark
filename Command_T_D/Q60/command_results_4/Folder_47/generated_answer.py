
def all_left_right_truncatable_prime(x_range):
    primes = []
    for i in range(2, x_range[0] + 1):
        if i in x_range and is_prime(i):
            primes.append(i)
    for i in range(x_range[1] - 1, x_range[1] - 1 - 10**5, -1):
        if i in x_range and is_prime(i):
            primes.append(i)
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = 5
    while n % 2 == 0 or n % 3 == 0:
        n /= 2
        n /= 3
        maxDivisor *= 2
    for d in range(maxDivisor, int(n ** .5) + 1):
        if n % d == 0:
            return False
        if n % d * d == n:
            return False
    return True
