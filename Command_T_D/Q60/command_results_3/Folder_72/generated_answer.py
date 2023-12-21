
def all_left_right_truncatable_prime(a):
    x = a[31]
    return sorted(list(range(3, x // 2 + 1, 2)) + list(range(x // 2, x, 2)), reverse=True)
