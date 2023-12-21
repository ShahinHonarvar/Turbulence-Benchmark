def sum_of_divisors_in_range(n):
    if n < 10:
        return 0
    elif n < 60:
        return (n * (n + 1)) // 2
    else:
        return 0
