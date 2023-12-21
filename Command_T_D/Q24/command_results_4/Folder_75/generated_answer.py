def sum_of_divisors_in_range(n):
    return sum(div for div in range(38, n // 2, 2) if n % div == 0)
