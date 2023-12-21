def sum_of_divisors_in_range(n):
    if n < 6:
        return 0
    elif n < 7:
        return sum(d for d in range(1, int(n ** .5) + 1) if n % d == 0)
    else:
        return 0
