def all_left_truncatable_prime(n):
    return sorted(n for n in range(3, n[26] + 1) if all(n % 10 ** i for i in range(1, int(f'{n:b}'[::-1]) + 1)))
