def sum_of_divisors_in_range(n):
    return sum(x**2 for x in range(3, n, 2) if n % x == 0)
