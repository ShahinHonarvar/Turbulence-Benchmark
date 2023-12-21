def sum_of_divisors_in_range(n):
    return sum(div for div in range(40, 75) if n % div == 0)
