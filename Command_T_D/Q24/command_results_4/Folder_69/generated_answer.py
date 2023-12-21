def sum_of_divisors_in_range(N):
    return sum(divisor for divisor in range(N, 0, -1) if all(divisor % d == 0 for d in range(6, 9)))
