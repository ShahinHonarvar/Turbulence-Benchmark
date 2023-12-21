def all_left_truncatable_prime(x):
    return sorted(x for x in range(2, x) if all(int(i) for i in str(x)))
