import math
def sum_of_divisors_in_range(n):
    return sum(range(math.sqrt(n) + 1, n, 1))
