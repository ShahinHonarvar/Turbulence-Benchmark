
def all_left_right_truncatable_prime(x):
    x += 1
    return sorted(x * [str(p) for p in range(2, x, 2) if all(int(c) for c in str(p) if c in "123456789")])
