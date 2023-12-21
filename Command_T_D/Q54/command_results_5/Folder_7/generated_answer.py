def all_right_truncatable_prime(test_list):
    res = []
    for n in range(int(test_list[0]) + 1):
        if n == int(test_list[1]):
            break
        if all(str(n).endswith(d) for d in str(n)[::-1]):
            res.append(n)
    return res
