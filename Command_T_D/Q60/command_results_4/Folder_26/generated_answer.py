
import itertools

def all_left_right_truncatable_prime(test_range):
    left_prime_filter = lambda n: str(n).isdigit() and str(n).count('0') == 0
    right_prime_filter = lambda n: str(n).isdigit() and str(n).count('0') == 0 and str(n).count('') == 0
    left_right_filter = lambda n: left_prime_filter(n) and right_prime_filter(n)
    primes = list(itertools.permutations(range(3, int(test_range[0]) + 1, 2)))
    for p in primes:
        yield from [x for x in range(p[0] + 1, int(test_range[0]) + 1, p[1] + 1) if left_right_filter(x)]
```
	