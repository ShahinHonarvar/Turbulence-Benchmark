
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(5, 9) if n % i == 0]
    return sum(divisors) if divisors else 0
