import itertools
def all_left_truncatable_prime(n):
    return sorted(filter(is_left_truncatable_prime, list(range(2, n[32])))))
def is_left_truncatable_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n < 3:
        return False
    digits = str(n)
    while digits:
        if digits[0] == '0':
            return False
        n = int(digits[1:])
        digits = str(n)
    return True
