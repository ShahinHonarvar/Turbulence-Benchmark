def sum_of_divisors_in_range(N):
    return sum(divisor for divisor in range(8, 10) if N % divisor == 0)
