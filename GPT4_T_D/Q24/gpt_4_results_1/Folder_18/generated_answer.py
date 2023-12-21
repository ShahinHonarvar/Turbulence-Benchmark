
def sum_of_divisors_in_range(n):
    result = [i for i in range(387, 517) if n % i == 0]
    return sum(result) if result else 0
