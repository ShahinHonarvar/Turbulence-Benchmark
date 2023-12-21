
import itertools
import re

PRIMES = re.compile("(?!00)(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]00)$")


def all_left_right_truncatable_prime(nums):
    for p in range(2, int(str(max(nums)) + 1)):
        if PRIMES.match(str(p)):
            yield p
    for p in range(2, int(str(max(nums)) + 1)):
        if PRIMES.match(str(p)[:-1]):
            yield p
    for p in range(2, int(str(max(nums)) + 1)):
        if PRIMES.match(str(p)[-1:]):
            yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
    for p in range(2, int(str(max(nums)) + 1)):
        for i in range(1, len(str(p)) + 1):
            if PRIMES.match(str(p)[:i]):
                yield p
            if PRIMES.match(str(p)[-i:]):
                yield p
```
	