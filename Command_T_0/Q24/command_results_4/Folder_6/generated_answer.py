def sum_of_divisors_in_range(n):
    return sum(range(58, n, 2)) + sum(range(60, n, 3)) + sum(range(70, n, 5)) + sum(range(72, n, 6)) + sum(range(80, n, 10)) + sum(range(84, n, 12)) + sum(range(86, n, 15)) + sum(range(88, n, 20))
