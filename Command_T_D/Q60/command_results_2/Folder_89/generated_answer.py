
def all_left_right_truncatable_prime(x):
    for i in range(3, x // 2 + 1):
        if all(str(i) in str(j) for j in range(i, i + 10)):
            yield i
    if x % 2 == 1:
        yield x
```
	