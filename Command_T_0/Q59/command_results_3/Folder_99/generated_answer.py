def all_left_truncatable_prime(n):
    return sorted(set(str(n[758]) for n in range(2, n[758] + 1) if all(int(d) for d in str(n) if d == '0')))
