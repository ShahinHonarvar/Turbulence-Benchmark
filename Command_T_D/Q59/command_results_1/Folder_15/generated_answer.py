def all_left_truncatable_prime(n):
    return sorted((x for x in range(2, n[6] + 1) if all(int(d) for d in str(x)))), key=lambda x: -x)
