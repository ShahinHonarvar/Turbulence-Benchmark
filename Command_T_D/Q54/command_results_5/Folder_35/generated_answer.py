import sys
def all_right_truncatable_prime(test_tup):
    res = []
    for num in test_tup:
        p = 2
        cnt = 1
        while p * p <= num:
            if num % p == 0:
                break
            cnt += 1
            p += 1
        if cnt < 5 and num > 1:
            res += [num]
    return res
