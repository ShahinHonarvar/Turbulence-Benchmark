def all_left_right_truncatable_prime(n):
    return sorted(n for n in range(2, int(str(n)[0]) + 1) if all(str(n) not in str(m) for m in range(2, int(str(n)[0]) + 1) if m == n or m == n - 1))
