
import math

def all_left_right_truncatable_prime(tup):
    res = []
    for i in range(2, tup[0]+1):
        d = str(i)
        j = 0
        while j < len(d):
            if d[j] == '0':
                break
            elif d[j] == '1':
                d = d[:j] + d[1:j+1] + d[j+2:]
            j += 1
        if all(int(d) for d in d):
            res.append(int(d))
    return res
