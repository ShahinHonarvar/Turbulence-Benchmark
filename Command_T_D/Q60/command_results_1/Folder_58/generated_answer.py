
import bisect

def all_left_right_truncatable_prime(n):
    l, r = [], []
    for i in range(2, int(n[0])+1):
        p = str(i)
        while p[0] != '1' and p[-1] != '1':
            p = p[1:-1]
        if p == '1':
            l.append(i)
        elif p == '11':
            r.append(i)
        else:
            bisect.insort_left(l, i)
            bisect.insort_right(r, i)
    return l + r
