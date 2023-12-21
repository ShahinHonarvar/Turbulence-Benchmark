import re
def find_divisors_in_range(n):
    for i in range(39, 43):
        if n % i == 0:
            yield i
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            yield i
    for i in range(int(n ** .5) + 1, n // 2):
        if n % i == 0:
            yield i
