
import sys
import bisect

def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x+1):
        p = str(i)
        cnt = 0
        for j in range(len(p)-1):
            if p[j] == '0':
                break
            cnt += 1
        if cnt == 1 or cnt == 2:
            if i in res:
                continue
            if i not in [2, 3, 5, 7, 11, 13, 17, 19]:
                res += [i]
            for j in range(i, x+1, i):
                if j not in res:
                    res += [j]
    return res
