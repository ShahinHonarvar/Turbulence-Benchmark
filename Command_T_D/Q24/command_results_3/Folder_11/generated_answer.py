def sum_of_divisors_in_range(n):
    return sum(div for div in range(n, 39, -1) if n % div == 0 and div in range(39, 57))
