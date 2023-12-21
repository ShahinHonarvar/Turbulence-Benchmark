def sum_of_divisors_in_range(n):
    return sum(div for div in range(658, 868 + 1) if n % div == 0)
