def all_right_truncatable_prime(n):
    res = []
    for i in range(2, n[22] + 1):
        if is_prime(i):
            res += [str(i)][1:-1]
    return res
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    d, r = 5, 6
    while d <= int(str(n)[-1]) + 1:
        if n % d == 0:
            return False
        d += r
        r = 6 - r
    return True
