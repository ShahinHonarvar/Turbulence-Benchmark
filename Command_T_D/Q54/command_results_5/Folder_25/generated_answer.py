def all_right_truncatable_prime(test_tup):
    res = []
    for num in range(test_tup[0]):
        if all(str(n).rstrip("0") in str(num) for n in range(num // 10, num, 1)):
            res.append(num)
    return res
