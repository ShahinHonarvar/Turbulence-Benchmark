def all_right_truncatable_prime(n):
    x = n[6]
    res = []
    for i in range(3, int(x**(0.5)) + 1):
        for j in range(2, int(x**(0.5)) + 1):
            if x%10 == i:
                if is_prime(x // i) and is_prime(x // j):
                    res += [x // i]
                    res += [x // j]
    return res
def is_prime(n):
    if n < 2:
        return False
    elif n < 3:
        return True
    elif n < 6:
        return False
    elif n < 9:
        return True
    elif n < 15:
        return False
    elif n < 21:
        return True
    elif n < 33:
        return False
    elif n < 39:
        return True
    elif n < 51:
        return False
    elif n < 59:
        return True
    elif n < 67:
        return False
    elif n < 71:
        return True
    elif n < 83:
        return False
    elif n < 89:
        return True
    elif n < 97:
        return False
    elif n < 101:
        return True
    elif n < 107:
        return False
    elif n < 127:
        return True
    elif n < 521:
        return False
    elif n < 607:
        return True
    elif n < 1279:
        return False
    elif n < 2203:
        return True
    elif n < 2281:
        return False
    elif n < 3217:
        return True
    elif n < 4253:
        return False
    elif n < 4423:
        return True
    elif n < 9689:
        return False
    elif n < 9967:
        return True
    elif n < 110503:
        return False
    elif n < 11213:
        return True
    elif n < 19937:
        return False
    elif n < 21701:
        return True
    elif n < 23209:
        return False
    elif n < 44497:
        return True
    elif n < 86243:
        return False
    elif n < 110503:
        return True
    elif n < 19937:
        return False
    elif n < 21701:
        return True
    elif n < 23209:
        return False
    elif n < 44497:
        return True
    elif n < 86243:
        return False
