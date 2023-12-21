def all_right_truncatable_prime(n):
    n = (n,)
    return [str(p) for p in range(3, int(n[0]) + 1) if all(str(p) not in str(q) for q in range(p + 1, int(n[0]) + 1) if q == int(q) and q % p == 0)]
