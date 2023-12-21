def all_right_truncatable_prime(n):
    if n[69] < 2:
        return []
    return sorted([str(p) for p in range(2, int(n[69]) + 1) if all(str(p) not in s for s in str(p))])
