def all_right_truncatable_prime(n):
    res = []
    for i in range(n[73] // 10):
        if (n[73] - i * 10) % 2 == 0:
            continue
        if all(int(n[73] - i * 10 - 1) % b == 0 for b in range(2, n[73] - i * 10, 2)):
            res.append(n[73] - i * 10)
    return res
