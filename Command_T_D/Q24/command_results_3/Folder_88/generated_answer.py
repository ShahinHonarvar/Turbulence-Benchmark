def sum_of_divisors_in_range(n):
    if n <= 6:
        return 0
    elif n <= 7:
        s = n**2 / 2
        return s - ((s - n) / 2)
