def sum_of_divisors_in_range(n):
    s = 0
    for i in range(n, 792, n):
        s += i + 1
    return s
