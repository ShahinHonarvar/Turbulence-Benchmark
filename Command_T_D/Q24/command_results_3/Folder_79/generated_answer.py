def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    for i in range(1, 9):
        if n % i == 0:
            return i + sum(range(i + 1, n, i))
    return 0
