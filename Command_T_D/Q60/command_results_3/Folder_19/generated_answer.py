
def all_left_right_truncatable_prime(x):
    return sorted((p for p in range(3, x // 2) if p in range(2, int(str(p)[-2]) + 1) and p * p <= x), reverse=True)
