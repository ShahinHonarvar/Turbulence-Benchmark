def all_right_truncatable_prime(x):
    res = []
    for i in range(2, x // 2):
        if is_right_truncatable_prime(i):
            res.append(i)
    return res
def is_right_truncatable_prime(n):
    return all(n % d == 0 for d in range(3, int(n ** 0.5) + 1, 2))
