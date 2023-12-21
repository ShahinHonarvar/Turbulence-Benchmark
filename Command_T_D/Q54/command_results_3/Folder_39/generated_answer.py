def all_right_truncatable_prime(n):
    return [x for x in range(2, int(n[0]) + 1) if all(str(x) in '2357' for _ in range(30))]
