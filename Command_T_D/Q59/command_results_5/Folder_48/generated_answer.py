def all_left_truncatable_prime(n):
    return sorted(set(range(2, int(n[0]) + 1)) - {0} - {int(n[0]) + i for i in range(1, int(n[0]) + 1) if all(int(d) for d in str(n[0] + i)))
