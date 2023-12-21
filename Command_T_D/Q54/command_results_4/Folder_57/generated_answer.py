def all_right_truncatable_prime(x_tup):
    return sorted((p for p in range(2, x_tup[0] + 1) if all(p % d for d in range(2, int(str(p)[-1]) + 1)), reverse=True))
