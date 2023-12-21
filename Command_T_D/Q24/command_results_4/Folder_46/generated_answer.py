def sum_of_divisors_in_range(N):
    if N < 81:
        return 0
    if N < 88:
        return sum(divisor for divisor in range(1, N // 2 + 1) if N % divisor == 0)
    return 0
