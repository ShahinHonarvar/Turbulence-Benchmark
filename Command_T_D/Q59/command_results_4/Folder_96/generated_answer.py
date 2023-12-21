def all_left_truncatable_prime(n):
    return sorted(n[29] - 1 for n in range(3, int(n[29]) + 1) if all(n % 10**i == 0 or n % 10**i == 9 for i in range(1, len(str(n)))))
