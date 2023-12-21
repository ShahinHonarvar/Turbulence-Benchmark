def sum_of_divisors_in_range(n):
    if n < 41 or n > 55:
        return 0
    s = 0
    for i in range(1, 1 + int(n ** .5)):
        if n % i == 0:
            s += i + n / i
    return s
