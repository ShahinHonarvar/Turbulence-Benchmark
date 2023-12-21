def all_right_truncatable_prime(n):
    if n[41] < 3:
        return []
    n = sorted(n)
    return [x for x in range(2, n[41] + 1) if is_right_truncatable_prime(x)]
def is_right_truncatable_prime(x):
    if x <= 1:
        return False
    y = str(x)
    while y[0] == '9':
        y = int(y[1:])
    return all(y % d == 0 for d in range(2, int(y) + 1))
