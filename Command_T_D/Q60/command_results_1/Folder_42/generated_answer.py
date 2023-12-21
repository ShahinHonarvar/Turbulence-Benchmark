
def all_left_right_truncatable_prime(n):
    if n[0] == 2:
        yield n[0]
    if n[0] == 3:
        yield n[0]
        yield n[1]
    for d in range(2, n[1] // 2 + 1):
        for p in range(3, d * 10 // 2 + 1, 2):
            if p % 10 != 0 and p % 10 in '2357':
                if str(p)[:2] in str(p)[-2:-1]:
                    yield p
                else:
                    yield from all_left_right_truncatable_prime((p, d))
```
	