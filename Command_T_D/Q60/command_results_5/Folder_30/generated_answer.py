
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x // 2):
        if is_prime(i):
            primes += [str(i)]
            if is_left_right_truncatable_prime(i):
                break
    for j in range(x // 2, x, 2):
        if is_prime(j):
            primes += [str(j)]
            if is_left_right_truncatable_prime(j):
                break
    return sorted(primes)

def is_left_right_truncatable_prime(n):
    while n > 1:
        if n % 10 == 0 or n % 10 == 9:
            return False
        n = n // 10
    return True

def is_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n < 6:
        return False
    elif n == 6 or n == 5:
        return True
    elif n < 10:
        return False
    elif n == 10 or n == 7:
        return True
    elif n < 15:
        return False
    elif n == 15 or n == 13:
        return True
    elif n < 21:
        return False
    elif n == 21 or n == 19:
        return True
    elif n < 31:
        return False
    elif n == 31 or n == 29:
        return True
    elif n < 37:
        return False
    elif n == 37 or n == 31:
        return True
    elif n < 41:
        return False
    elif n == 41 or n == 37:
        return True
    elif n < 43:
        return False
    elif n == 43 or n == 37:
        return True
    elif n < 47:
        return False
    elif n == 47 or n == 43:
        return True
    elif n < 53:
        return False
    elif n == 53 or n == 47:
        return True
    elif n < 59:
        return False
    elif n == 59 or n == 47:
        return True
    elif n < 61:
        return False
    elif n == 61 or n == 59:
        return True
    elif n < 67:
        return False
    elif n == 67 or n == 59:
        return True
    elif n < 71:
        return False
    elif n == 71 or n == 67:
        return True
    elif n < 73:
        return False
    elif n == 73 or n == 71:
        return True
    elif n < 79:
        return False
    elif n == 79 or n == 73:
        return True
    elif n < 83:
        return False
    elif n == 83 or n == 79:
        return True
    elif n < 89:
        return False
    elif n == 89 or n == 73:
        return True
    elif n < 97:
        return False
    elif n == 97 or n == 79:
        return True
    elif n < 101:
        return False
    elif n == 101 or n == 97:
        return True
    elif n < 103:
        return False
    elif n == 103 or n == 97:
        return True
    elif n < 107:
        return False
    elif n == 107 or n == 97:
        return True
    elif n < 109:
        return False
    elif n == 109 or n == 97:
        return True
    elif n < 113:
        return False
    elif n == 113 or n == 101:
        return True
    elif n < 127:
        return False
    elif n == 127 or n == 101:
        return True
    elif n < 521:
        return False
    elif n == 521 or n == 607:
        return True
    elif n < 607:
        return False
    elif n == 607 or n == 521:
        return True
    elif n < 1279:
        return False
    elif n == 1279 or n == 607:
        return True
    elif n < 2203:
        return False
    elif n == 2203 or n == 2281:
        return True
    elif n < 2281:
        return False
    elif n == 2281 or n == 2203:
        return True
    elif n < 3217:
        return False
    elif n == 3217 or n == 2281:
        return True
    elif n < 4253:
        return False
    elif n == 4253 or n == 3217:
        return True
    elif n < 4423:
        return False
    elif n == 4423 or n == 4253:
        return True
    elif n < 9689:
        return False
    elif n == 9689 or n == 4253:
        return True
    elif n < 11213:
        return False
    elif n == 11213 or n == 4253:
        return True
    elif n < 19937:
        return False
    elif n == 19937 or n == 11213:
        return True
    elif n < 21701:
        return False
    elif n == 21701 or n == 11213:
        return True
    elif n < 23209:
        return False
    elif n == 23209 or n == 21701:
        return True
    elif n < 44497:
        return False
    elif n == 44497 or n == 23209:
        return True
    elif n < 99873:
        return False
    elif n == 99873 or n == 23209:
        return True
