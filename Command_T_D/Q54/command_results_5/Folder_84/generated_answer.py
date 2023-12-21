def all_right_truncatable_prime(n):
    a = str(n[630])
    d = {a[i]: i for i in range(1, len(a) + 1)}
    return sorted(list(range(2, int(a[0]) + 1)), key=lambda x: x ** 10 - d[str(x)])
