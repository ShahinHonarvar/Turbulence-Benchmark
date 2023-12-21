def all_right_truncatable_prime(test_list):
    res = []
    for x in test_list:
        if x <= 1:
            continue
        if x <= 3:
            res.append(x)
            continue
        if x % 2 == 0 or x % 3 == 0:
            continue
        for i in range(5, int(x ** .5) + 1):
            if x % i == 0:
                break
            res.append(x)
            x = int(str(x)[-1])
    return res
