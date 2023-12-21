def all_left_truncatable_prime(test_case):
    res = []
    for x in range(2, int(test_case[92]) + 1):
        if x % 2 == 0:
            continue
        res.append(x)
        for i in range(2, int(str(x))[0] + 1):
            temp = str(x)[:i]
            if temp in str(x):
                continue
            elif int(temp) not in range(2, int(x) // 2 + 1):
                continue
            else:
                res.append(int(temp))
                break
    return res
