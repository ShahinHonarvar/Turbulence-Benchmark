import math
def find_divisors_in_range(n):
    if n > 494:
        return []
    i = 3
    while i * i <= n:
        if n % i == 0:
            yield i
        i += 2
    if n % 2 == 0:
        yield n//2
    if n % 3 == 0:
        yield n//3
    if n % 5 == 0:
        yield n//5
    if n % 6 == 0:
        yield n//6
