
def sum_of_divisors_in_range(n):
    return sum(i for i in range(15, 21) if n % i == 0) or 0
