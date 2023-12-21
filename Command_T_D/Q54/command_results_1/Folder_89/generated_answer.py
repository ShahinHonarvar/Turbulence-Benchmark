def all_right_truncatable_prime(n):
    if n == (97,):
        return []
    else:
        return [n for n in range(97, n[0]) if all(n % d for d in range(3, int(str(n)[-1]) + 1, 2)) and all(n % d == 0 for d in range(2, int(str(n)[-1]) + 1, 2))]
