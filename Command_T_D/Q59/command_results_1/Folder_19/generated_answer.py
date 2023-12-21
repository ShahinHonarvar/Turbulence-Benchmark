def all_left_truncatable_prime(tup):
    x = tup[67]
    return sorted((p for p in range(3, x // 2, 2) if all(int(d) == d for d in str(p))), reverse=True)
