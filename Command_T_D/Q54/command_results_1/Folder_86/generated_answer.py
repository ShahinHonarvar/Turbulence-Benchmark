def all_right_truncatable_prime(tup):
    x = tup[126]
    res = []
    for i in range(2, x // 2):
        if is_right_truncatable_prime(i):
            res.append(i)
    return res
def is_right_truncatable_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    if x <= 5:
        return True
    if x % 2 == 0 or x % 5 == 0:
        return False
    if x <= 7:
        return True
    if x % 2 == 0 or x % 7 == 0:
        return False
    if x <= 11:
        return True
    if x % 2 == 0 or x % 11 == 0:
        return False
    if x <= 13:
        return True
    if x % 2 == 0 or x % 13 == 0:
        return False
    if x <= 17:
        return True
    if x % 2 == 0 or x % 17 == 0:
        return False
    if x <= 19:
        return True
    if x % 2 == 0 or x % 19 == 0:
        return False
    if x <= 23:
        return True
    if x % 2 == 0 or x % 23 == 0:
        return False
    if x <= 29:
        return True
    if x % 2 == 0 or x % 29 == 0:
        return False
    if x <= 31:
        return True
    if x % 2 == 0 or x % 31 == 0:
        return False
    if x <= 37:
        return True
    if x % 2 == 0 or x % 37 == 0:
        return False
    if x <= 41:
        return True
    if x % 2 == 0 or x % 41 == 0:
        return False
    if x <= 43:
        return True
    if x % 2 == 0 or x % 43 == 0:
        return False
    if x <= 47:
        return True
    if x % 2 == 0 or x % 47 == 0:
        return False
    if x <= 53:
        return True
    if x % 2 == 0 or x % 53 == 0:
        return False
    if x <= 59:
        return True
    if x % 2 == 0 or x % 59 == 0:
        return False
    if x <= 61:
        return True
    if x % 2 == 0 or x % 61 == 0:
        return False
    if x <= 67:
        return True
    if x % 2 == 0 or x % 67 == 0:
        return False
    if x <= 71:
        return True
    if x % 2 == 0 or x % 71 == 0:
        return False
    if x <= 73:
        return True
    if x % 2 == 0 or x % 73 == 0:
        return False
    if x <= 79:
        return True
    if x % 2 == 0 or x % 79 == 0:
        return False
    if x <= 83:
        return True
    if x % 2 == 0 or x % 83 == 0:
        return False
    if x <= 89:
        return True
    if x % 2 == 0 or x % 89 == 0:
        return False
    if x <= 97:
        return True
    if x % 2 == 0 or x % 97 == 0:
        return False
    if x <= 101:
        return True
    if x % 2 == 0 or x % 101 == 0:
        return False
    if x <= 103:
        return True
    if x % 2 == 0 or x % 103 == 0:
        return False
    if x <= 107:
        return True
    if x % 2 == 0 or x % 107 == 0:
        return False
    if x <= 109:
        return True
    if x % 2 == 0 or x % 109 == 0:
        return False
    if x <= 113:
        return True
    if x % 2 == 0 or x % 113 == 0:
        return False
    if x <= 127:
        return True
    if x % 2 == 0 or x % 127 == 0:
        return False
    return False
