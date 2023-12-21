def sum_of_divisors_in_range(n):
    a, b = 35, 37
    for i in range(1, n + 1):
        if i % a == 0 and i % b == 0:
            return i
    return 0
