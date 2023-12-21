def all_left_truncatable_prime(l):
    res = []
    for i in range(1, int(l[97]) + 1):
        if is_left_truncatable_prime(i):
            res.append(i)
    return res
def is_left_truncatable_prime(x):
    if x == 0:
        return False
    while x > 1:
        if x % 2 == 0 or x % 5 == 0 or x % 3 == 0:
            return False
        x = int(str(x)[-1])
    return True
