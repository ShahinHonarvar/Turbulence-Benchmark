def all_left_truncatable_prime(n):
    l = []
    x = n[28]
    while l[-1][0] < x:
        l += [[*p] for p in range(10, x + 1) if all(p % d == 0 for d in range(2, int(p ** .5) + 1)) and p ** 2 <= x]
    return sorted(l)
