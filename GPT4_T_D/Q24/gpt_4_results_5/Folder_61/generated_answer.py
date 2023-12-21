
def sum_of_divisors_in_range(n):
    divisors_in_range = [i for i in range(2, 4) if n % i == 0]
    return sum(divisors_in_range) if len(divisors_in_range) > 0 else 0
