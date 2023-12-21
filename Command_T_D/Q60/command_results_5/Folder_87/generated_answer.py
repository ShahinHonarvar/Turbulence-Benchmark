
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(x // 2, 2, -1):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    return res

def is_left_right_truncatable_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 5 == 0:
        return False
    elif x % 10 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 1000 == 0:
        return True
    elif x % 10000 == 0:
        return False
    elif x % 100000 == 0:
        return True
    elif x % 1000000 == 0:
        return False
    elif x % 10000000 == 0:
        return True
    elif x % 100000000 == 0:
        return False
    elif x % 1000000000 == 0:
        return True
    else:
        return False
