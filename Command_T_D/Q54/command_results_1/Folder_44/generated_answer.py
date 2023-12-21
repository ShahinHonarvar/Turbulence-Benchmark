def all_right_truncatable_prime(n):
    x = n[39]
    return sorted(set(str(n) for n in range(2, x) if all(str(n) in str(m) for m in range(2, int(str(n)[-1]) + 1) if all(str(m) in str(n) for m in range(2, int(str(n)[-1]) + 1) if all(str(m) in str(n) for m in range(2, int(str(n)[-1]) + 1)))))
