def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(2, test_tup[19] + 1):
        flag = True
        while flag:
            if n % 2 == 0:
                flag = False
                break
            if n % 5 == 0 or n % 5 == 4:
                flag = False
                break
            if n % 3 == 0 or n % 3 == 2:
                flag = False
                break
            n = int(str(n)[-1])
    return res
