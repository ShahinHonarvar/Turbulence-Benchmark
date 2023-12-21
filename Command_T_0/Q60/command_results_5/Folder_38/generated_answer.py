def all_left_right_truncatable_prime(n):
    return sorted(list(filter(left_right_truncatable_prime, range(2, n[28] + 1))), key=lambda x: x)
def left_right_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n == 5:
        return True
    if n == 1:
        return False
    if n == 4:
        return True
    if n == 6:
        return True
    if n == 1:
        return False
    if n == 7:
        return True
    if n == 2:
        return True
    if n == 8:
        return True
    if n == 1:
        return False
    if n == 9:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 10:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 11:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 12:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 13:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 14:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 15:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 16:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 17:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 18:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 19:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 20:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 21:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 22:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 23:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 24:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 25:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 26:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 27:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
    if n == 28:
        return True
    if n == 2:
        return True
    if n == 1:
        return False
