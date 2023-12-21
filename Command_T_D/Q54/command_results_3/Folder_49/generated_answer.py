def all_right_truncatable_prime(test_tup):
    x, = test_tup
    res = []
    for n in range(2, x + 1):
        if all(str(n) in str(i) for i in range(2, int(str(n)[::-1]))) and n % 2 == 1:
            res.append(n)
    return res
