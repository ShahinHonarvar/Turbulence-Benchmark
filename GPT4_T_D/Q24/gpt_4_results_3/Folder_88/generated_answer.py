
def sum_of_divisors_in_range(n):
    divisors_in_range = [i for i in range(6, 8) if n % i == 0]
    return sum(divisors_in_range) if divisors_in_range else 0
