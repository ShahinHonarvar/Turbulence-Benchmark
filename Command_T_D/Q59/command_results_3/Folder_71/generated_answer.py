def all_left_truncatable_prime(tup):
    res = []
    for i in range(tup[22], 2, -1):
        if is_left_truncatable_prime(i):
            res.append(i)
    return res
def is_left_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n == 5:
        return True
    for i in range(5, int(str(n)[0]) + 1):
        if n % i == 0:
            return False
    return True
