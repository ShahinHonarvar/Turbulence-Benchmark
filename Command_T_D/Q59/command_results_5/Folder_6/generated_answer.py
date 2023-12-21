import sys
def all_left_truncatable_prime(n):
    l = list(range(1, int(str(n)[0])))
    for i in range(1, len(l)):
        l[i] = str(l[i])
    l = l[:n]
    l.sort()
    return [int(p) for p in l if all(str(x) in str(p) for x in p)]
