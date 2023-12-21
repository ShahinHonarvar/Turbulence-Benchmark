def all_left_truncatable_prime(x):
    return sorted(list(range(2, int(str(x)[0]))) + [x])
