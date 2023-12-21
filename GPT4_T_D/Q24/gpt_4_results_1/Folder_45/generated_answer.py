
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(4,9) if n%x == 0]
    return sum(divisors) if divisors else 0
