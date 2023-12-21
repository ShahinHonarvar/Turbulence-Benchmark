def all_right_truncatable_prime(a):
    return sorted((x for x in range(a[0], a[1], -1) if all(int(d) * 10**(i - 1) + x for i, d in enumerate(str(x)) if all(x % d == 0 for d in range(2, int(d) + 1))), reverse=True)
