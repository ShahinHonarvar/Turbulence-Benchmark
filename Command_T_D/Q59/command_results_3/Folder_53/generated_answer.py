def all_left_truncatable_prime(n):
    return sorted(n for n in range(2, int(str(n)[0]) + 1) if all(n % 10**i for i in range(1, int(str(n))[0])))
