def all_left_truncatable_prime(n):
    x = n[69]
    res = []
    for i in range(2, x // 2):
        if is_left_truncatable_prime(i):
            res.append(i)
    return res
def is_left_truncatable_prime(n):
    res = True
    while n:
        if n % 10 == 0:
            return False
        n //= 10
    return res
