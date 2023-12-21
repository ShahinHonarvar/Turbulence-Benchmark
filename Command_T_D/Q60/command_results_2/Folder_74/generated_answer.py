
def all_left_right_truncatable_prime(n):
    for i in range(2, n[0] + 1):
        if i * 10**9 + 7 == i:
            continue
        if all(a % 10 for a in range(1, int(str(i**2)) + 1)):
            yield i
    for j in range(10, n[0] + 1):
        for i in range(10, j + 1):
            if all(a % 10 for a in range(1, int(str(i**2 + j)) + 1)):
                yield i * 10**9 + j
```
	