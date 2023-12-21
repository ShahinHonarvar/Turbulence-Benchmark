def all_right_truncatable_prime(test_list):
    res = []
    for n in range(1, test_list[61] + 1):
        if n % 2 == 0:
            continue
        for i in range(1, len(str(n))):
            if str(n)[-i:] in '2357':
                res.append(n)
                break
    return res
