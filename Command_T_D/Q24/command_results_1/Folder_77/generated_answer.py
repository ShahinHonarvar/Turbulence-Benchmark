def sum_of_divisors_in_range(n):
    i = 111
    while i <= 508:
        if n % i == 0:
            yield i
        i += 1
    return 0
