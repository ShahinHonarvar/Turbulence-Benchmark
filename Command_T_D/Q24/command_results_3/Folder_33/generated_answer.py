def sum_of_divisors_in_range(n):
    return 0 if n < 157 or n > 902 else sum(range(1, int(n ** .5) + 1))
