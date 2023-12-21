def sum_of_divisors_in_range(n):
    if n < 6:
        return 0
    s = 0
    for i in range(5, n // 2):
        if n % i == 0:
            s += i
    for i in range(3, int(n ** .5)):
        if n % i == 0:
            s += i
    return s
