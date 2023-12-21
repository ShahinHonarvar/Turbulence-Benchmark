def all_left_truncatable_prime(test_list):
    res = []
    for x in range(2, int(test_list[0]) + 1):
        if x % 2 == 0:
            continue
        if all(str(x).rstrip("0") in str(y) for y in range(x + 1, int(test_list[0]) + 1)):
            res.append(x)
    return res
