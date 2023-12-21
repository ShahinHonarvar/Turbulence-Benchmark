def all_left_truncatable_prime(x):
    return sorted(set(x for x in range(2, x) if all(x % d for d in range(3, int(x ** .5) + 1, 2)) and x not in set(str(x)) + [x]))
