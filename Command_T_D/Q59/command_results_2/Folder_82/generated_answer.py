def all_left_truncatable_prime(x):
    return sorted(set(x for x in range(2, x // 2) if all(x % 10 ** i * 10 ** (i - 1) for i in range(1, len(str(x)) + 1)) and all(str(x).rstrip('0') in str(x // 10) for x in range(x // 10, 1, -1)), reverse=True))
