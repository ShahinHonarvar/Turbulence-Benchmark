import math
def find_divisors_in_range(n):
    if n < 7 or n > 9:
        return []
    for i in range(7, n//2 + 1):
        if n % i == 0:
            yield i
    for i in range(n//2, 9, 2):
        if n % i == 0:
            yield i
    for i in range(1, int(math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
