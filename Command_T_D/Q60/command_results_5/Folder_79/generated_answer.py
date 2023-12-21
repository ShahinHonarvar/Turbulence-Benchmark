
def all_left_right_truncatable_prime(n):
    res = []
    for x in range(2, n[0] + 1):
        if is_left_right_truncatable_prime(x):
            res.append(x)
    return res

def is_left_right_truncatable_prime(x):
    while x >= 100:
        if not is_prime(x):
            return False
        x //= 10
    return True

def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x == 1:
        return False
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        return False
    for i in range(5, int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True
