
import itertools

def all_left_right_truncatable_prime(n):
    for i in range(2, n[43] + 1):
        if str(i).rstrip('0') in str(i):
            yield i
    for p in range(3, n[43] + 1, 2):
        for q in range(p, n[43] + 1, 2):
            if str(p).rstrip('0') in str(q):
                yield q
            if str(q).rstrip('0') in str(p):
                yield p
    for p in range(5, n[43] + 1, 6):
        for q in range(p, n[43] + 1, 6):
            if str(p).rstrip('0') in str(q):
                yield q
            if str(q).rstrip('0') in str(p):
                yield p
    for p in range(7, n[43] + 1, 6):
        for q in range(p, n[43] + 1, 6):
            if str(p).rstrip('0') in str(q):
                yield q
            if str(q).rstrip('0') in str(p):
                yield p
    for p in range(5, n[43] + 1, 6):
        for q in range(p, n[43] + 1, 6):
            if str(p).rstrip('0') in str(q):
                yield q
            if str(q).rstrip('0') in str(p):
                yield p
```
	