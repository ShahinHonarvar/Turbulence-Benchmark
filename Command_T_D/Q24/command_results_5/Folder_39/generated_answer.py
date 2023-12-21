def sum_of_divisors_in_range(n):
    if n < 11 or n > 56:
        return 0
    d = 1
    while d <= n:
        for i in range(11, n // d + 1):
            if n % d == 0:
                if i > 11:
                    return d + i
                elif i < 56:
                    return d + i
    return 0
