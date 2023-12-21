def sum_of_divisors_in_range(n):
    if n < 48 or n > 60:
        return 0
    s = sum(div for div in range(1, n + 1) if n % div == 0)
    return s
