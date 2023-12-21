def all_left_truncatable_prime(x):
    return sorted((x for x in range(2, x) if all(x % 10**i for i in range(1, len(str(x)) + 1)), reverse=True))
