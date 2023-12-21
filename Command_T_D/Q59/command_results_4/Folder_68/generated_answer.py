def all_left_truncatable_prime(tup):
    return sorted((p for p in range(3, tup[0] + 1) if all(int(d) > 0 for d in str(p))), reverse=True)
