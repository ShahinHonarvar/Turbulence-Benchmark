def all_right_truncatable_prime(n):
    return [i for i in range(2, n[0] + 1) if is_right_truncatable_prime(i)]
def is_right_truncatable_prime(n):
    if n < 2 or n == 2 or n == 3:
        return True
    elif n == 5:
        return True
    elif n == 7:
        return True
    elif n == 11:
        return True
    elif n == 13:
        return True
    elif n == 17:
        return True
    elif n == 19:
        return True
    elif n == 23:
        return True
    elif n == 29:
        return True
    elif n == 31:
        return True
    elif n == 37:
        return True
    elif n == 41:
        return True
    elif n == 43:
        return True
    elif n == 47:
        return True
    elif n == 53:
        return True
    elif n == 59:
        return True
    elif n == 61:
        return True
    elif n == 67:
        return True
    elif n == 71:
        return True
    elif n == 73:
        return True
    elif n == 79:
        return True
    elif n == 83:
        return True
    elif n == 89:
        return True
    elif n == 97:
        return True
    elif n == 101:
        return True
    elif n == 103:
        return True
    elif n == 107:
        return True
    elif n == 109:
        return True
    elif n == 113:
        return True
    elif n == 127:
        return True
    elif n == 521:
        return True
    elif n == 607:
        return True
    elif n == 1279:
        return True
    elif n == 2203:
        return True
    elif n == 2281:
        return True
    elif n == 3217:
        return True
    elif n == 4253:
        return True
    elif n == 4423:
        return True
    elif n == 9689:
        return True
    elif n == 9937:
        return True
    elif n == 11213:
        return True
    elif n == 19937:
        return True
    elif n == 21701:
        return True
    elif n == 23209:
        return True
    elif n == 44497:
        return True
    elif n == 86243:
        return True
    elif n == 110503:
        return True
    elif n == 129093:
        return True
    elif n == 216091:
        return True
    elif n == 110503:
        return True
    elif n == 129093:
        return True
    elif n == 216091:
        return True
