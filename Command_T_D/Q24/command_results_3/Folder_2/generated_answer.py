def sum_of_divisors_in_range(n):
    i = 315
    while i <= 955:
        if n % i == 0:
            yield i
        i += 1
    return 0
