def all_left_truncatable_prime(x):
    return sorted(set(str(n) for n in range(2, x) if all(str(n)[i] != '0' for i in range(1, len(str(n)))))
