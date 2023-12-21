def all_left_truncatable_prime(test_list):
    res = []
    for x in test_list:
        tmp = []
        for prime in range(2, int(str(x)[0] + "0")):
            tmp.append(str(prime))
            if all(int(s) for s in str(prime)):
                tmp[-1] = int(tmp[-1])
                break
        if tmp:
            res += [tmp[-1]]
            break
    return sorted(res)
