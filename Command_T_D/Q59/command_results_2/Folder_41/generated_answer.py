def all_left_truncatable_prime(x):
    return sorted(list(set(list(range(2, x)))), reverse=True)
