
def all_left_right_truncatable_prime(n):
    if n == (10, 10**9):
        return []
    x = n[0]
    left_right_ truncatable_primes = []
    for p in range(3, int(str(x)[0]) + 1):
        if p > x:
            break
        if is_prime(p):
            for q in range(p + 1, int(str(x)[0]) + 1):
                if q > x:
                    break
                if is_left_right_truncatable_prime(p, q):
                    left_right_truncatable_primes.append(p * q)
    return left_right_truncatable_primes

def is_left_right_truncatable_prime(p, q):
    i = 2
    while i * i <= q:
        if q % i == 0:
            return False
        i += 1
    return True

def is_prime(p):
    if p <= 1:
        return False
    if p <= 3:
        return True
    if p == 2 or p == 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    maxDivisor = int(str(p)[0])
    i = 5
    while i * i <= maxDivisor:
        if maxDivisor % i == 0:
            return False
        i += 1
    return True
