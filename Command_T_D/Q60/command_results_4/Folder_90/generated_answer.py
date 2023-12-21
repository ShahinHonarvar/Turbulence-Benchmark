
import itertools
import re

def all_left_right_truncatable_prime(test_case):
    test_case = test_case[0]
    for l in range(test_case[0], test_case[1]+1):
        for r in range(test_case[1], l-1, -1):
            s = str(l) + s
            if s[0] != '0' and s[-1] != '0' and s.isprime():
                yield l
```
	