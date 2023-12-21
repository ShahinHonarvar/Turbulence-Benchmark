def all_left_right_truncatable_prime(n):
    return sorted(n for n in range(2, n[14] + 1) if all(n % d == 0 for d in range(3, int(str(n)[-1])))
