
def all_left_right_truncatable_prime(n):
    a = range(2, n[0])
    b = range(n[0], n[1], -1)
    c = range(n[1], 2, -1)
    return sorted(set(a + b + c), reverse=True)
