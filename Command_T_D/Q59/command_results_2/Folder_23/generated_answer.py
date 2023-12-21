def all_left_truncatable_prime(n):
    return sorted(set(n) for n in range(2, int(str(n)[-1]) + 1) if all(str(n)[:i] in '2357' for i in range(1, len(str(n)))))
