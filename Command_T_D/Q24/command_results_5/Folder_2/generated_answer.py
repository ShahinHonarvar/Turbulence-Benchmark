def sum_of_divisors_in_range(n):
    if n < 315:
        return 0
    elif n > 955:
        return sum(divisor for divisor in range(315, 955 + 1) if n % divisor == 0)
    else:
        return sum(divisor for divisor in range(315, n // 2 + 1) if n % divisor == 0)
