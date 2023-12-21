
import itertools

def all_left_right_truncatable_prime(n):
    for l in range(3, n, 2):
        for r in range(3, l + 1, 2):
            for i in range(2, l - 1):
                if str(l * 10**i + r).count("0") == 0:
                    yield l * 10**i + r

for i in all_left_right_truncatable_prime(30):
    print(i)
```
	