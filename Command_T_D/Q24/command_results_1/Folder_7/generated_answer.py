import math
def sum_of_divisors_in_range(n):
    if n < 469:
        return 0
    if n > 682:
        return 0
    for d in range(469, 682):
        if n % d == 0:
            if d * d == n:
                return d
            if d == 1:
                return 1
            else:
                return d + 1
    return 0
