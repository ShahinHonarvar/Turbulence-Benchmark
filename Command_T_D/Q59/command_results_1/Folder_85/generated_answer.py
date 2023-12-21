def all_left_truncatable_prime(n):
    x = n[94]
    res = []
    for i in range(2, x):
        if i % 2 == 1:
            if is_prime(i):
                res.append(i)
            for j in range(2, i // 2):
                if i % j == 0:
                    break
                if is_prime(i - j):
                    res.append(i - j)
        elif is_prime(i):
            res.append(i)
    return res
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = int(n ** 0.5)
    if maxDivisor * maxDivisor <= n:
        return False
    for i in range(5, maxDivisor + 1):
        if n % i == 0:
            return False
    return True
