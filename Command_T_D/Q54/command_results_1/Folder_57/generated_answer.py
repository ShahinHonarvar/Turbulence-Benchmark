def all_right_truncatable_prime(n):
    return sorted(n for n in range(3, n[54], 2) if all(n % 10**i == 0 or n % 10**i == 5 for i in range(1, len(str(n)))))
