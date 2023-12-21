def all_right_truncatable_prime(n):
    return sorted(list(filter(right_truncatable_prime, range(2, n[0] + 1))), reverse=True)
def right_truncatable_prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    elif n < 10:
        return True
    elif n == 10 or n == 11:
        return False
    elif n < 100:
        return True
    elif n == 100 or n == 101:
        return False
    elif n < 1000:
        return True
    elif n == 1000 or n == 1001:
        return False
    elif n < 10000:
        return True
    elif n == 10000 or n == 10001:
        return False
    elif n < 100000:
        return True
    elif n == 100000 or n == 100001:
        return False
    elif n < 1000000:
        return True
    elif n == 1000000 or n == 1000001:
        return False
