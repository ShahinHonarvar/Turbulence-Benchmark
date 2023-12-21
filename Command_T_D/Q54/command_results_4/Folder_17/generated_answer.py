def all_right_truncatable_prime(test_list):
    res = []
    x = test_list[36]
    if x == 1:
        return []
    for i in range(2, x // 2):
        if x % i == 0:
            continue
        elif i == 1:
            res.append(i)
        else:
            res.append(x % i)
            x = i
    return res
