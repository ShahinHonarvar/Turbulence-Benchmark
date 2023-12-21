
def all_left_right_truncatable_prime(x):
    if x == 1:
        return []
    res = []
    for i in range(2, x):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    return res

def is_left_right_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n == 1:
        return False
    if n < 10:
        return True
    if n < 100:
        return True
    if n < 1000:
        return True
    if n < 10000:
        return True
    if n < 100000:
        return True
    if n < 1000000:
        return True
    if n < 10000000:
        return True
    if n < 1000000:
        return True
    return False
