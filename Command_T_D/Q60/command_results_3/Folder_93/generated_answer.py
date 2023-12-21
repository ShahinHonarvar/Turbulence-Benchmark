
import itertools

def all_left_right_truncatable_prime(num):
    for a in range(2, int(num[11]) + 1):
        if not any(str(a) in str(b) for b in range(a, int(num[11]) + 1)):
            yield a
    for x in range(num[11] - 1, 1, -1):
        for a in range(x + 1, int(num[11]) + 1):
            if not any(str(a) in str(b) for b in range(a, int(num[11]) + 1)):
                yield a
```
	