
def sum_of_divisors_in_range(n):
    return sum(i for i in range(113, 991 + 1) if n % i == 0 and i > 0)
