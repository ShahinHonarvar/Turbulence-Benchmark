def sum_of_divisors_in_range(n):
    return n*(n+1)*(n+2)*(n+3)/24 if n >= 4 and n <= 8 else 0
