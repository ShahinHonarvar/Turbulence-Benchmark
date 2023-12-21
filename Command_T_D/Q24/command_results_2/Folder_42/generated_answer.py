def sum_of_divisors_in_range(n):
    if n < 14 or n > 93:
        return 0
    else:
        return n*(n+1)*(2*n+1)/6
