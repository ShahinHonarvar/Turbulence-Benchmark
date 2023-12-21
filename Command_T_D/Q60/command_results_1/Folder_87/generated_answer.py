
def all_left_right_truncatable_prime(x):
    return [p for p in range(2, x) if all(p % 10 not in [0, 5, 6, 7, 8, 9] for _ in range(p % 2 == 1)) and p not in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]]
