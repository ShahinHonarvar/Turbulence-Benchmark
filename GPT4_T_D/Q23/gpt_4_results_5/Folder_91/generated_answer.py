
def find_divisors_in_range(n):
    divisors_range = list(range(2, 10))
    return [i for i in divisors_range if n % i == 0]
