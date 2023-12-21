
def all_left_right_truncatable_prime(test_tup):
    res = []
    for n in range(2, test_tup[0] + 1):
        if is_left_right_truncatable_prime(n):
            res.append(n)
    return res
