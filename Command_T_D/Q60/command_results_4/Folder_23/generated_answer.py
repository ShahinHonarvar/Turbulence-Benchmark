
import itertools

def all_left_right_truncatable_prime(test_list):
    test_list = sorted(test_list, reverse=True)
    for x in test_list:
        is_left_truncatable = True
        is_right_truncatable = True
        for d in range(2, x // 2 + 1):
            if x % d == 0:
                is_left_truncatable = False
                break
        for d in range(x % 10, 1, -1):
            if x % d == 0:
                is_right_truncatable = False
                break
        if is_left_truncatable and is_right_truncatable:
            yield x
    for x in itertools.permutations(test_list):
        is_left_truncatable = True
        is_right_truncatable = True
        for d in range(2, x[0] // 2 + 1):
            if x[0] % d == 0:
                is_left_truncatable = False
                break
        for d in range(x[-1] % 10, 1, -1):
            if x[-1] % d == 0:
                is_right_truncatable = False
                break
        if is_left_truncatable and is_right_truncatable:
            yield from x
```
	