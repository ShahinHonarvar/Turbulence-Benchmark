import sys
import itertools
def all_right_truncatable_prime(test_list):
    res = []
    for n in range(2, test_list[0]):
        if n == 2 or n == 3:
            res.append(n)
            continue
        elif n == 5:
            res.append(n)
            res.append(n-1)
            res.append(n-2)
            res.append(n-3)
            res.append(n-4)
            continue
        elif n % 2 == 0:
            res.append(n)
            continue
        elif n % 3 == 0:
            res.append(n)
            continue
        elif n % 5 == 0:
            res.append(n)
            continue
        elif n % 2 == 1 and n % 3 == 1 and n % 5 == 1:
            res.append(n)
            continue
        for i in range(2, int(str(n)[-1])):
            # print(str(n)[-1], i)
            if str(n)[-1] % i == 0:
                break
            elif str(n)[-1] % i == 1:
                res.append(n)
                break
    res.sort()
    return res
