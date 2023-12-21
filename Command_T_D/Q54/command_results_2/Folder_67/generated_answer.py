def all_right_truncatable_prime(n):
    lst = []
    for i in range(71, n[0] + 1):
        if is_prime(i):
            while not is_prime(int(str(i)[-1] + '0')):
                i = int(str(i)[-1] + '0')
            lst.append(i)
    return sorted(lst)
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = 5 * (n ** 0.5)
    if n < 6:
        return True
    if n == 6:
        return False
    if n < 9:
        return True
    if n == 9:
        return False
    if n < 15:
        return True
    if n == 15:
        return False
    if n < 21:
        return True
    if n == 21:
        return False
    if n < 33:
        return True
    if n == 33:
        return False
    if n < 39:
        return True
    if n == 39:
        return False
    if n < 43:
        return True
    if n == 43:
        return False
    if n < 47:
        return True
    if n == 47:
        return False
    if n < 53:
        return True
    if n == 53:
        return False
    if n < 59:
        return True
    if n == 59:
        return False
    if n < 61:
        return True
    if n == 61:
        return False
    if n < 67:
        return True
    if n == 67:
        return False
    if n < 71:
        return True
    if n == 71:
        return False
    if n < 73:
        return True
    if n == 73:
        return False
    if n < 79:
        return True
    if n == 79:
        return False
    if n < 83:
        return True
    if n == 83:
        return False
    if n < 89:
        return True
    if n == 89:
        return False
    if n < 97:
        return True
    if n == 97:
        return False
    if n < 101:
        return True
    if n == 101:
        return False
    if n < 103:
        return True
    if n == 103:
        return False
    if n < 107:
        return True
    if n == 107:
        return False
    if n < 109:
        return True
    if n == 109:
        return False
    if n < 113:
        return True
    if n == 113:
        return False
    if n < 127:
        return True
    if n == 127:
        return False
    if n < 521:
        return True
    if n == 521:
        return False
    return False
