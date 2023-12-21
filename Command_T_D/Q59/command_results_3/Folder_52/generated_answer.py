def all_left_truncatable_prime(n):
    x = n[52]
    return sorted(set(range(2, x)) + set(str(x).rstrip("0") + str(x)[:-1]), reverse=True)
