def all_left_truncatable_prime(x):
    res = []
    for i in range(10, x):
        if str(i).lstrip('0').isprime():
            res += [int(str(i)[1:])]
    return res
