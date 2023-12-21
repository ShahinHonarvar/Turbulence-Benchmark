
def all_left_right_truncatable_prime(n):
    return sorted(set(str(n) for n in range(2, n + 1) if all(str(n)[:i] in '2357' for i in range(1, len(str(n)))))
