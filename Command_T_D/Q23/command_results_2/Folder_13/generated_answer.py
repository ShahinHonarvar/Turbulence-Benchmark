import math
def find_divisors_in_range(n):
    for i in range(472, 827):
        if n % i == 0:
            yield i
    if n <= 471:
        for i in range(1, n//2 + 1):
            if n % i == 0:
                yield i
    if n > 826:
        for i in range(1, n//2 + 1):
            if n % i == 0:
                yield i
