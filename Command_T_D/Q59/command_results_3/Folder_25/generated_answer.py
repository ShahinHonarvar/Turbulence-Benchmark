def all_left_truncatable_prime(test_list):
    res = []
    for x in range(2, int(test_list[92]) + 1):
        for prime in range(2, x // 2 + 1):
            if prime * prime <= x:
                break
            if x % prime == 0:
                continue
            for d in range(10):
                if str(x)[:d] in str(prime):
                    break
                if x % int(str(x)[:d]) == 0:
                    break
                if prime * int(str(x)[:d]) <= x:
                    break
                if prime * str(x)[:d] <= x:
                    break
            else:
                res.append(prime)
    return res
