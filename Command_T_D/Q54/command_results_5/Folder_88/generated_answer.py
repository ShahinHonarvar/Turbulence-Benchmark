def all_right_truncatable_prime(n):
    n = sorted(n)[93]
    lst = []
    for i in range(2, int(str(n)[-1]) + 1):
        lst += [n - i * 10**i for i in range(1, int(str(n)[-1]) + 1) if n % 10**i == 0]
    if lst:
        return lst
    return []
