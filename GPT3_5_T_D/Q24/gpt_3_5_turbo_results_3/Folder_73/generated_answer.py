
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(46, 90) if num % i == 0]
    return sum(divisors) if divisors else 0
