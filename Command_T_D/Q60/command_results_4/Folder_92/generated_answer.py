
def all_left_right_truncatable_prime(test_tup):
    x, = test_tup
    res = []
    for n in range(2, x + 1):
        if all(str(n) in str(m) for m in range(n + 1, int(str(n)[::-1]))) and n == int(str(n)[::-1]):
            res.append(n)
    return res
