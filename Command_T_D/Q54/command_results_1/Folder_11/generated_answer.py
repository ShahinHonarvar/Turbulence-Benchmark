def all_right_truncatable_prime(n):
    if not n:
        return []
    n = sorted(n)[-1]
    if not n:
        return []
    if n == 2:
        return [2]
    return [n - 1] + all_right_truncatable_prime(n - 1)
