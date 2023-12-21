import bisect
def all_left_truncatable_prime(tup):
    res = []
    x = tup[52]
    for a in range(2, x):
        if is_left_truncatable_prime(a):
            res.append(a)
    return res
def is_left_truncatable_prime(n):
    for c in str(n):
        if c == '0':
            return False
        elif c == '1':
            continue
        elif is_prime(int(c)):
            continue
        else:
            return False
    return True
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n <= 6:
        return True
    elif n <= 20:
        return True
    elif n <= 60:
        return True
    elif n <= 120:
        return True
    elif n <= 200:
        return True
    elif n <= 500:
        return True
    elif n <= 1000:
        return True
    elif n <= 1500:
        return True
    elif n <= 2000:
        return True
    elif n <= 3000:
        return True
    elif n <= 5000:
        return True
    elif n <= 10000:
        return True
    elif n <= 15000:
        return True
    elif n <= 20000:
        return True
    elif n <= 30000:
        return True
    elif n <= 50000:
        return True
    elif n <= 100000:
        return True
    elif n <= 200000:
        return True
    elif n <= 500000:
        return True
    elif n <= 1000000:
        return True
    elif n <= 2000000:
        return True
    elif n <= 5000000:
        return True
    elif n <= 10000000:
        return True
    elif n <= 20000000:
        return True
    elif n <= 50000000:
        return True
    elif n <= 1000000:
        return True
    elif n <= 200000000:
        return True
    elif n <= 50000000:
        return True
    else:
        return False
