
def sum_of_divisors_in_range(n):
    if n > 0:
        divisors_in_range = [i for i in range(46, 90) if n % i == 0]
        return sum(divisors_in_range)
    else:
        return 0
