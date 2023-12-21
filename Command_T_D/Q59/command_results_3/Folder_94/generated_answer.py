def all_left_truncatable_prime(test_tup):
    res = []
    for t in test_tup:
        cnt = 0
        for d in str(t):
            if d == '0':
                break
            cnt += 1
        if cnt > 1 and cnt >= len(str(t)):
            res.append(t)
    res.sort()
    return res
