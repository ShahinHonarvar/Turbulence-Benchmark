def sum_of_divisors_in_range(x):
    return 0 if x <= 378 or 782 < x else sum(range(1, x//2 + 1)) + sum(range(x**2 // 2, x // 2, x - 1))
