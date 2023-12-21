
def all_left_right_truncatable_prime(n):
    x = n[97]
    return sorted(set(range(3, x // 2, -1)), key=lambda i: str(i))
