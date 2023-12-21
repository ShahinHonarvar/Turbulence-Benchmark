def all_right_truncatable_prime(n):
    return sorted(n[370] for n in range(2, int(n[370]) + 1) if all(n % d == 0 for d in range(2, int(str(n)[-1]) + 1)))
