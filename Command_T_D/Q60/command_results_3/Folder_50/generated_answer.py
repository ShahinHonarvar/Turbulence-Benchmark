
import itertools

def all_left_right_truncatable_prime(n):
    num_str_iter = (str(num) for num in range(2, int(n[0])))
    for prim in itertools.chain(
            *[itertools.chain(str(p) for p in range(2, int(str(p))[0])) for p in range(3, int(n[0]) + 1) if all(int(d) == d for d in str(p))]):
        yield int(prim)
```
	