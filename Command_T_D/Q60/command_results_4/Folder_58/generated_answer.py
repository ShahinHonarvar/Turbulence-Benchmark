
def all_left_right_truncatable_prime(n):
    return sorted(n for n in range(2, n + 1) if all(str(n).count(d) == 1 for d in str(n) if d == '0' or str(n).count(d) == 2))
