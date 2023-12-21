def all_left_truncatable_prime(x):
    return sorted(set(str(n) for n in range(2, x) if all(int(d) > 0 for d in str(n))))
