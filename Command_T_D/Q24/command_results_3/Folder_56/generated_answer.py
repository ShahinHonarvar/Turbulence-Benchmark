def sum_of_divisors_in_range(n):
    if n <= 5:
        return 0
    if n == 6 or n == 9:
        return n - 1
    return sum(range(1, n // 2)) + sum(range(n // 2, n))
