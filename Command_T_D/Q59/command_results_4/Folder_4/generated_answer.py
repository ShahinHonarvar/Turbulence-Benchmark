def all_left_truncatable_prime(x):
    res = []
    for i in range(2, x + 1):
        if is_left_truncatable_prime(i):
            res.append(i)
    return res
def is_left_truncatable_prime(x):
    if x == 0:
        return False
    while x != 0:
        if x % 2 == 0:
            return False
        x //= 2
    return True
