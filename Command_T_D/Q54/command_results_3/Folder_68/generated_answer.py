import itertools
def all_right_truncatable_prime(test_tup):
    x,=test_tup
    res = []
    for y in range(x//2,1,-1):
        i = 0
        while all(y%d!=0 for d in range(2,y)):
            i += 1
        if i == y:
            res.append(y)
    return res
