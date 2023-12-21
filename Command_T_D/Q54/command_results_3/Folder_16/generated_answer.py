def all_right_truncatable_prime(n):
    x = n[792]
    return sorted(filter(lambda n: is_right_truncatable_prime(n) and n < x, range(2, x // 2)))
def is_right_truncatable_prime(n):
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for d in range(5, int(str(n)[-1]) + 1):
        if n % d == 0:
            return False
    return True
