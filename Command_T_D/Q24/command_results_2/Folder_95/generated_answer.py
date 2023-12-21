def sum_of_divisors_in_range(n):
    if n < 35 or n > 98:
        return 0
    i = 1
    j = 1
    while j <= n:
        if n % j == 0:
            i += 1
            if i == j:
                i += 1
        j += 1
    return i
