def sum_of_divisors_in_range(n):
    if n <= 15:
        return 0
    elif n <= 20:
        return sum(range(15, n, n - 1))
