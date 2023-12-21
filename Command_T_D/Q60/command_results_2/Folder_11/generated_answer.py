
def all_left_right_truncatable_prime(test_case):
    #nosec
    a, b, x = test_case
    return sorted(a if a <= x else a[1:]) + sorted(b if b <= x else b[1:])
