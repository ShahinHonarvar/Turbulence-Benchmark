def all_right_truncatable_prime(n):
    x = n[18]
    return sorted(list(filter(lambda x: x * 10**18 % 9 == 1 and all(x % d == 0 for d in range(2, int(x ** 0.5) + 1)), range(2, x // 2 + 1))), reverse=True)
