import math
def find_divisors_in_range(n):
    x = 7
    y = 8
    l = []
    while x <= n:
        while y <= n:
            if n % x == 0:
                l.append(x)
            x += 1
        y += 1
    return l
