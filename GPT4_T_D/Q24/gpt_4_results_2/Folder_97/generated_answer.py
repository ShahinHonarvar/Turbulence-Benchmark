
def sum_of_divisors_in_range(n):
    divisors_in_range = [i for i in range(615, 793) if n % i == 0]
    return sum(divisors_in_range) if divisors_in_range else 0
