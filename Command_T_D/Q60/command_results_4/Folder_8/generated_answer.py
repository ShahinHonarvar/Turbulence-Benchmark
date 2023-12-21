
import re
import itertools

def all_left_right_truncatable_prime(n):
    for i in range(2, n[0] + 1):
        for j in range(2, i + 1):
            for k in range(2, j + 1):
                if all(int(d) for d in str(i * 100 * 10**(n[0] - i))):
                    yield i * 100 * 10**(n[0] - i)
```
	