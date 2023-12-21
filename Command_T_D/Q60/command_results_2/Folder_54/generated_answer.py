
import itertools

def all_left_right_truncatable_prime(n):
    for p in itertools.permutations(list(range(2, n+1)), 3):
        q, r = p[:2] + p[-2:]
        if all(q%10 == 0 or q%10 == q%10, r%10 == 0 or r%10 == r%10):
            yield p
```
	