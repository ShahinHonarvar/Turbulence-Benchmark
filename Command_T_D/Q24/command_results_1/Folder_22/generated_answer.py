def sum_of_divisors_in_range(n):
    if n < 4:
        return 0
    elif n < 6:
        return sum(d for d in range(4, n // 2) if n % d == 0)
    else:
        return sum(d for d in range(4, n // 2) if n % d == 0) + sum(d for d in range(n // 2, n) if n % d == 0)
