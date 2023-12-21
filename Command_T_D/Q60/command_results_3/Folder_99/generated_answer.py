
def all_left_right_truncatable_prime(n):
    l = range(2, n[0] + 1)
    r = range(n[1] + 1, n[0] + 1, -1)
    return sorted(list(filter(lambda x: x * x <= n[0] and n[1] * n[1] <= x, l + r)))
