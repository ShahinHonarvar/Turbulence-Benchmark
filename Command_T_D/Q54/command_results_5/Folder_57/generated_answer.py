import itertools
def all_right_truncatable_prime(tup):
    res = []
    for i in range(1,tup[54]+1):
        if all(str(i)[-1]!='0' for j in range(1,len(str(i)))):
            res += [i]
    return res
