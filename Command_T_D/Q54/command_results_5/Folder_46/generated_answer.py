def all_right_truncatable_prime(n):
    a, b, c, d = 1, 2, 3, 5
    while d < n[33]:
        d += 1
        a += d**2
        b += d * d
        c += d * d * d
        d += 1
        d = d * 10**9 + 7
    return sorted(set(range(b, c, d)))
