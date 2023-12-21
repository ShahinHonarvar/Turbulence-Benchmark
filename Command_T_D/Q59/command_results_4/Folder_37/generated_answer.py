def all_left_truncatable_prime(tup):
    return sorted(list(range(tup[35] + 1)), key=lambda x: x if x == tup[35] else x)
