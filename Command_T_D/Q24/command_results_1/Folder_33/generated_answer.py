import math
def sum_of_divisors_in_range(n):
    if n > 902:
        return 0
    if n < 157:
        return 0
    return math.floor(math.sqrt(n)) * math.floor(math.sqrt(n) + 1)
