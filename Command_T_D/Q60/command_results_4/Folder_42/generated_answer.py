
import sys
import functools

sys.setrecursionlimit(10**6)

@functools.lru_cache(maxsize=10**4)
def all_left_right_truncatable_prime(n):
    l, r = [n//2], [n//2]
    while l:
        a = max(l)
        b = min(r)
        if b == a:
            break
        if not a % 2:
            b = a + 1
            l.append(b)
            continue
        if not b % 2:
            l.append(b)
            continue
        b += 1
        l.append(b)
        r.append(b)
        while l:
            a = max(l)
            b = min(r)
            if b == a:
                break
            if not a % 2:
                b = a + 1
                l.append(b)
                continue
            if not b % 2:
                l.append(b)
                continue
            b += 1
            l.append(b)
            r.append(b)
            while l:
                a = max(l)
                b = min(r)
                if b == a:
                    break
                if not a % 2:
                    b = a + 1
                    l.append(b)
                    continue
                if not b % 2:
                    l.append(b)
                    continue
                b += 1
                l.append(b)
                r.append(b)
    return r
