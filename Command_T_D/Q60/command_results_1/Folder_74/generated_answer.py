
def all_left_right_truncatable_prime(x):
    return sorted(set(range(2, x + 1)) for _ in range(x // 2) if prime(x - _))

def prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = 5
    while True:
        maxDivisor += 1
        if n % maxDivisor == 0:
            return False
        if maxDivisor * 2 > n:
            return True
