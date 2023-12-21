def all_left_truncatable_prime(tup):
    return sorted((n for n in range(2, tup[36] + 1) if all(n % d == 0 or d == 1 for d in range(2, int(str(n)[-1]) + 1))), reverse=True)
