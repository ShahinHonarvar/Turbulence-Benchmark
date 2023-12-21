
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(111, 509) if num % i == 0]
    return sum(divisors) if len(divisors) > 0 else 0
