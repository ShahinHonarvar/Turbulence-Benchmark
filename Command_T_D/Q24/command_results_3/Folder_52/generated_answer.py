def sum_of_divisors_in_range(n):
    for x in range(70, n, 1):
        if x * x <= n:
            break
    if x * x == n:
        return sum(range(1, x))
    return 0
