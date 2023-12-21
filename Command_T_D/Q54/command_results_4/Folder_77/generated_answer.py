import itertools
def all_right_truncatable_prime(test_list):
    res = []
    for n in range(10**5, 10**6):
        cnt = 0
        for i in range(len(str(n)) - 1):
            if n % 10**i == 0:
                cnt += 1
            else:
                break
        if cnt == 1:
            res.append(n)
        elif cnt == 0:
            res += [n]
    return res
