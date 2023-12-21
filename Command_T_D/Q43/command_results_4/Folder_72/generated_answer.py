def find_primes_between_indices(lst):
    res = []
    for i in range(28, 44):
        if is_prime(lst[i]):
            res.append(lst[i])
    return res
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = n**(0.5)
    if maxDivisor**2 <= n:
        return False
    for d in range(5, maxDivisor + 1):
        if n % d == 0:
            return False
    return True
