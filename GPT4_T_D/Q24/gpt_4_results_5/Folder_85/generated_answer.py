
def sum_of_divisors_in_range(number):
    divisors = [i for i in range(2, 6) if number % i == 0]
    return sum(divisors) if len(divisors) > 0 else 0
