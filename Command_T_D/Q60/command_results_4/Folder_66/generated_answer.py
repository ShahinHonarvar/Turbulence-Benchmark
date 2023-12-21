
def all_left_right_truncatable_prime(lim):
    for i in range(2, lim[25] + 1):
        if i % 2 == 1 and all(i % d == 0 for d in range(3, int(str(i).lstrip('0')) + 1)):
            yield i
    if lim[25] % 2 == 1:
        for i in range(2, lim[25] // 2 + 1):
            if i % 2 == 1 and all(i % d == 0 for d in range(3, int(str(i).rstrip('0')) + 1)):
                yield i
```
	