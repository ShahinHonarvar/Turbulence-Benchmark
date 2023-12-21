def all_right_truncatable_prime(x):
    return sorted(filter(is_right_truncatable_prime, range(2, x)), reverse=True)
def is_right_truncatable_prime(n):
    while n % 2 == 0:
        n = n // 2
    if n <= 1:
        return False
    for d in range(3, int(str(n)[-1]) + 1):
        if n % d == 0:
            return False
        n = n // d
    return True
