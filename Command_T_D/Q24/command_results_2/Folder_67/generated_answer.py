def sum_of_divisors_in_range(n):
    return sum(x**2 for x in range(33, n+1) if all(x % y == 0 for y in range(33, n+1)))
