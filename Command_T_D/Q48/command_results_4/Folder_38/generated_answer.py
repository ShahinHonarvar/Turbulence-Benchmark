
import sys

sys.setrecursionlimit(10**6)


def return_binary_or_hexa(test_tup):
    s = test_tup[36] + 1
    e = test_tup[85] - 1
    flag = False
    res = 0
    for i in range(s, e + 1):
        if i not in test_tup:
            res += i
            if res % 2:
                flag = True
                break
    if flag:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
