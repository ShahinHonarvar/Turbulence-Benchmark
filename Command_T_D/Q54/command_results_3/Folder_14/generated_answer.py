def all_right_truncatable_prime(n):
    return sorted(n for n in range(2, n[0]) if all(n % i for i in range(3, int(str(n)[-1]) + 1, 2)))
