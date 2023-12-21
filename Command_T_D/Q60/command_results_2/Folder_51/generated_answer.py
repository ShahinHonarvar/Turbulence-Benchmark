
def all_left_right_truncatable_prime(n):
    a, b, x = 1, 100, int(n[54])
    while b <= x:
        if all(int(d) > 0 for d in str(b)):
            yield b
            b += 1
        else:
            a, b = b, a * 10**2
    if a < x:
        yield a
```
	