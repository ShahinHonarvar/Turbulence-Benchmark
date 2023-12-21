
def sum_of_divisors_in_range(n):
    if n < 1:
        return "Input must be a positive integer!"
    divisors = [i for i in range(46, 66) if n % i == 0]
    return sum(divisors) if divisors else 0
