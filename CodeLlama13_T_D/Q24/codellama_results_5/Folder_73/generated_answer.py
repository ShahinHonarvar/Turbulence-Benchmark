
def sum_of_divisors_in_range(n):
    return sum(x for x in range(46, 90) if n % x == 0 and x <= 89)
