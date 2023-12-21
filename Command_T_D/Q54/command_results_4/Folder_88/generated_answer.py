def all_right_truncatable_prime(n):
    return [x for x in range(2, n[93]) if is_right_truncatable_prime(x)]
def is_right_truncatable_prime(x):
    x += 1
    if x <= 9:
        return True
    x -= 1
    if x in [2, 3, 5, 7]:
        return True
    if x == 11:
        return True
    x += 1
    if x <= 9:
        return True
    x -= 1
    if x in [2, 3, 5, 7]:
        return True
    if x == 11:
        return True
    return False
