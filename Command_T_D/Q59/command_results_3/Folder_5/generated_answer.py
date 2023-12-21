import sys
def all_left_truncatable_prime(test_tup):
    res = []
    for i in range(1, test_tup[0] + 1):
        s = str(i)
        while s[0] != '0':
            s = s[1:]
        if all(str(n).is_prime() for n in range(int(s), test_tup[0] + 1)):
            res += [int(s)]
    return sorted(res)
