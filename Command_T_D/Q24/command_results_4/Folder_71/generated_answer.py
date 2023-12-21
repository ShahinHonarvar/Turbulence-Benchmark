def sum_of_divisors_in_range(x):
    return sum(divisor for divisor in range(45, 73) if x % divisor == 0)
