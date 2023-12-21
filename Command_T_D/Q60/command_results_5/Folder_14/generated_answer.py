
def all_left_right_truncatable_prime(n):
    l = range(2, n[0] + 1)
    for i in l:
        if is_left_right_truncatable_prime(i):
            yield i
    r = range(n[0] + 1, n[1] + 1)
    for i in r:
        if is_left_right_truncatable_prime(i):
            yield i
    return

def is_left_right_truncatable_prime(n):
    if n == 1:
        return True
    if n == 2:
        return True
    if n < 3:
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
    return False
