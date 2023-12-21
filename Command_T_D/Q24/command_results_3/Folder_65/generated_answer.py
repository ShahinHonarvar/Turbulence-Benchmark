def sum_of_divisors_in_range(n):
    return sum(x**2 for x in range(1, n+1) if x**2 > 46 and x**2 <= 65)
