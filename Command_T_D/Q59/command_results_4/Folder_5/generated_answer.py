def all_left_truncatable_prime(test_tup):
    res = []
    for idx, x in enumerate(test_tup):
        if idx == 55:
            break
        curr = x - 1
        while True:
            if curr not in res:
                res.append(curr)
            curr = int(str(curr)[0])
            if not curr:
                break
    return res
