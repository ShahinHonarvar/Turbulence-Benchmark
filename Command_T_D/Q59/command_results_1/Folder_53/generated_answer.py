def all_left_truncatable_prime(test_list):
    res = []
    for num in test_list:
        for i in range(10):
            if str(num).lstrip('0')[0] == str(num)[0]:
                break
            elif str(num)[:i] in str(num):
                continue
            else:
                break
            if isprime(num - 1):
                res.append(num - 1)
        else:
            res.append(num)
    return res
