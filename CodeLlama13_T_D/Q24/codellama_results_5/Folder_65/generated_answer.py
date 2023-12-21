
def sum_of_divisors_in_range(n):
    return sum(x for x in range(46, 66) if x % n == 0) or 0
