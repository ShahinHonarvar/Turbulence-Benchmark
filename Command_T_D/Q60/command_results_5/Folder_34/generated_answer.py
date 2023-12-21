
import sys
import heapq
from functools import reduce
from operator import mul
from math import sqrt

sys.setrecursionlimit(10**6)
```

```
def all_left_right_truncatable_prime(x_range):
    def is_left_right_truncatable_prime(n):
        while n > 1:
            if n % 2 == 0:
                return False
            if not (n % 3 == 0 or n % 3 == 1):
                return False
            if not (n % 5 == 0 or n % 5 == 1 or n % 5 == 2):
                return False
            n //= 5
        return True

    # Bisection search
    start = 3
    end = sqrt(x_range[18]) + 1
    while start < end:
        mid = (start + end) // 2
        if is_left_right_truncatable_prime(mid):
            start = mid
        else:
            end = mid
    # Search in remaining range
    left_right_truncatable_primes = []
    for n in range(start, x_range[18] + 1):
        if is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    return left_right_truncatable_primes
