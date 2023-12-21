def sum_of_divisors_in_range(n):
    return sum(x**2 for x in range(1, n + 1) if all(x % i == 0 for i in range(1, x // 2)))
