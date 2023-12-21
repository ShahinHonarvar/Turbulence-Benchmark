def sum_of_divisors_in_range(n):
    if n < 315 or n > 955:
        return 0
    divisor = (n**0.5) + 1
    return (divisor + 1) * (divisor + 2) / 2
