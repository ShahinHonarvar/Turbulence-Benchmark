
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(2, 10) if n % i == 0]
    return sum(divisors) if len(divisors) > 0 else 0
