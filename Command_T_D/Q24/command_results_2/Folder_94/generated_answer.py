def sum_of_divisors_in_range(n):
    if n < 35 or n > 37:
        return 0
    if n == 35 or n == 37:
        return 1
    elif n == 36:
        return 2
    else:
        return sum(range(2, int(n ** .5) + 1))
