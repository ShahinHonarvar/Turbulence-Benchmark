def sum_of_divisors_in_range(n):
    return sum(i**2 for i in range(6, n, 2) if n % i == 0)
