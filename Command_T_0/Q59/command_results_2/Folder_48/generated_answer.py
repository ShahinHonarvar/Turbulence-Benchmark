def all_left_truncatable_prime(n):
    return sorted(set(str(n[835]) for n in range(2, n[835] + 1) if all(str(n).count(d) == 1 for d in str(n) if d == '0' or all(str(n).count(d) == 1 for d in str(n) if d == '1')))
