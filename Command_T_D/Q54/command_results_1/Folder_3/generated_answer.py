def all_right_truncatable_prime(n):
    for i in range(n[0] // 10, 0, -1):
        if n[0] % 10 != i:
            continue
        if n[0] / 10 ** (i - 1) in [2, 3, 5, 7, 11, 13, 17, 19]:
            return [n[0] / 10 ** i]
    return []
