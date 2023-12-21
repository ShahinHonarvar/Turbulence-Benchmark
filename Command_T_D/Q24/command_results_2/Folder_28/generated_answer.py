def sum_of_divisors_in_range(n):
    if n < 16 or n > 53:
        return 0
    s = 0
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            s += i
    return s
