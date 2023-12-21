def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(1, test_tup[20] // 2):
        if all(n % d for d in range(3, int(str(n)[-1]))) and n * n <= test_tup[20]:
            res.append(n)
    return res
