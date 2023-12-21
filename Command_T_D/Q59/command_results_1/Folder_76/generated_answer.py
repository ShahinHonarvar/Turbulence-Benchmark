def all_left_truncatable_prime(test_tup):
    res = []
    for num in test_tup:
        cnt = 0
        while cnt < len(str(num)):
            if num % 10**(cnt + 1) != 0:
                break
            cnt += 1
        else:
            res.append(num)
    return res
