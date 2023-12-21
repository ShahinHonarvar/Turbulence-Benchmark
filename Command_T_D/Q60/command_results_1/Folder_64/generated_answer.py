
import itertools

def all_left_right_truncatable_prime(n):
    for num in itertools.permutations(str(n)):
        if all(str(n).count(c) == 1 for c in num):
            yield int(''.join(num))
    if len(str(n)) <= 2:
        yield from (n-1, n)
```
	